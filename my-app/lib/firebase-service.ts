import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
} from 'firebase/auth';
import {
  collection,
  doc,
  setDoc,
  getDoc,
  updateDoc,
  addDoc,
  query,
  where,
  orderBy,
  limit,
  getDocs,
  serverTimestamp,
  Timestamp,
} from 'firebase/firestore';
import { auth, db } from './firebase';
import type { UserData, Payment, AppNotification, Referral, Reward, Withdrawal, SignUpFormData } from './types';
import { ACTIVATION_AMOUNT, TOTAL_ACTIVATION, REWARD_CASHBACK, REWARD_BONUS, REWARD_TOTAL, REWARD_DELAY_WEEKS, CAMPAIGN_END_DATE } from './constants';

// ── SMS helper ────────────────────────────────────────────────────────────────

function sendSMSNotification(to: string, message: string): void {
  if (typeof window === 'undefined' || !to) return;
  fetch('/api/send-sms', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ to, message }),
  }).catch(() => {});
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function generateReferralCode(): string {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  return Array.from({ length: 8 }, () => chars[Math.floor(Math.random() * chars.length)]).join('');
}

function getCommissionRate(count: number): number {
  if (count >= 20) return 100;
  if (count >= 10) return 75;
  if (count >= 1) return 50;
  return 0;
}

function getTierLabel(count: number): string {
  if (count >= 20) return 'Platinum';
  if (count >= 10) return 'Gold';
  if (count >= 1) return 'Silver';
  return 'Starter';
}

export function formatDate(value: Timestamp | Date | null | undefined): string {
  if (!value) return '-';
  const d = value instanceof Date ? value : value.toDate();
  return d.toLocaleDateString('en-ZA', { day: '2-digit', month: 'short', year: 'numeric' });
}

export function isCampaignActive(): boolean {
  return new Date() < CAMPAIGN_END_DATE;
}

// ── Auth ──────────────────────────────────────────────────────────────────────

export async function signUpUser(
  email: string,
  password: string,
  userData: SignUpFormData
): Promise<{ success: boolean; uid?: string; referralCode?: string; error?: string }> {
  try {
    if (!isCampaignActive()) {
      throw new Error('This special offer has ended. Please contact support.');
    }

    const cred = await createUserWithEmailAndPassword(auth, email, password);
    const uid = cred.user.uid;

    let referralCode = generateReferralCode();
    for (let i = 0; i < 10; i++) {
      const snap = await getDocs(
        query(collection(db, 'users'), where('referralCode', '==', referralCode), limit(1))
      );
      if (snap.empty) break;
      referralCode = generateReferralCode();
    }

    let referredBy: string | null = null;
    if (typeof window !== 'undefined') {
      const refCode =
        new URLSearchParams(window.location.search).get('ref') ||
        localStorage.getItem('referralCode');
      if (refCode) {
        const snap = await getDocs(
          query(collection(db, 'users'), where('referralCode', '==', refCode), limit(1))
        );
        if (!snap.empty && snap.docs[0].id !== uid) {
          referredBy = snap.docs[0].id;
        }
      }
    }

    const now = serverTimestamp();
    await setDoc(doc(db, 'users', uid), {
      uid,
      email,
      fullName: userData.fullName,
      phone: userData.phone,
      idNumber: userData.idNumber,
      employmentStatus: userData.employmentStatus,
      source: userData.source,
      planType: userData.planType,
      tier: userData.tier,
      referralCode,
      referredBy,
      referredByName: userData.referredByName,
      beneficiary: userData.beneficiary,
      spouse: userData.spouse,
      dependents: userData.dependents,
      extendedFamily: userData.extendedFamily,
      isActivated: false,
      totalPaid: 0,
      activationDate: null,
      rewardReleaseDate: null,
      families: [],
      funeralCoverActive: false,
      funeralCoverExpiry: null,
      applicationStatus: 'submitted',
      createdAt: now,
      updatedAt: now,
    });

    if (referredBy) {
      await addDoc(collection(db, 'referrals'), {
        referrerId: referredBy,
        referredUserId: uid,
        referredUserName: userData.fullName,
        status: 'signed_up',
        commissionAmount: 0,
        paidAt: null,
        createdAt: now,
      });
      await createNotification(
        referredBy,
        'joined',
        `${userData.fullName || 'Someone'} joined using your referral link!`
      );
      const referrerSnap = await getDoc(doc(db, 'users', referredBy));
      if (referrerSnap.exists() && referrerSnap.data().phone) {
        sendSMSNotification(
          referrerSnap.data().phone as string,
          `GoDirect247: ${userData.fullName || 'Someone'} just joined using your referral link! Get them to activate and earn your commission.`
        );
      }
    }

    return { success: true, uid, referralCode };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Unknown error' };
  }
}

export async function loginUser(
  email: string,
  password: string
): Promise<{ success: boolean; uid?: string; error?: string }> {
  try {
    const cred = await signInWithEmailAndPassword(auth, email, password);
    return { success: true, uid: cred.user.uid };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Login failed' };
  }
}

export async function logoutUser(): Promise<void> {
  await signOut(auth);
}

export async function getUserData(uid: string): Promise<UserData | null> {
  const snap = await getDoc(doc(db, 'users', uid));
  if (!snap.exists()) return null;
  return { id: snap.id, ...snap.data() } as UserData;
}

// ── Admin ─────────────────────────────────────────────────────────────────────

export async function checkIsAdmin(uid: string): Promise<boolean> {
  try {
    const snap = await getDoc(doc(db, 'admins', uid));
    return snap.exists();
  } catch {
    return false;
  }
}

export async function getAllMembers(): Promise<{
  success: boolean;
  members?: (UserData & { id: string })[];
  error?: string;
}> {
  try {
    const snap = await getDocs(query(collection(db, 'users'), orderBy('createdAt', 'desc')));
    const members = snap.docs.map((d) => {
      const data = { id: d.id, ...d.data() } as UserData & { id: string };
      if (!data.status) data.status = data.isActivated ? 'Active' : 'Pending';
      return data;
    });
    return { success: true, members };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Failed to load members' };
  }
}

export async function getPendingPayments(): Promise<{
  success: boolean;
  payments?: Payment[];
  error?: string;
}> {
  try {
    const snap = await getDocs(
      query(collection(db, 'payments'), where('status', '==', 'pending'), orderBy('createdAt', 'desc'))
    );
    const payments = snap.docs.map((d) => ({ id: d.id, ...d.data() } as Payment));
    return { success: true, payments };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Failed to load payments' };
  }
}

export async function verifyPayment(
  paymentId: string,
  adminId: string
): Promise<{ success: boolean; error?: string }> {
  try {
    const now = serverTimestamp();
    const paymentRef = doc(db, 'payments', paymentId);
    const paymentSnap = await getDoc(paymentRef);
    if (!paymentSnap.exists()) throw new Error('Payment not found');
    const payment = paymentSnap.data() as Payment;

    await updateDoc(paymentRef, { status: 'paid', verifiedBy: adminId, verifiedAt: now, paidAt: now });

    const userRef = doc(db, 'users', payment.userId);
    const userSnap = await getDoc(userRef);
    if (!userSnap.exists()) throw new Error('User not found');
    const user = userSnap.data() as UserData;

    const newTotalPaid = (user.totalPaid || 0) + payment.amount;
    const updates: Record<string, unknown> = { totalPaid: newTotalPaid, updatedAt: now };

    const isSelfActivation = payment.type === 'self' && payment.amount >= ACTIVATION_AMOUNT;
    const isFullyPaid = newTotalPaid >= TOTAL_ACTIVATION && !user.isActivated;

    if ((isSelfActivation || isFullyPaid) && !user.isActivated) {
      const rewardDate = new Date();
      rewardDate.setDate(rewardDate.getDate() + REWARD_DELAY_WEEKS * 7);
      const rewardTs = Timestamp.fromDate(rewardDate);
      const coverExpiry = new Date();
      coverExpiry.setMonth(coverExpiry.getMonth() + 12);

      updates.isActivated = true;
      updates.activationDate = now;
      updates.rewardReleaseDate = rewardTs;
      updates.funeralCoverActive = true;
      updates.funeralCoverExpiry = Timestamp.fromDate(coverExpiry);

      if (isFullyPaid) {
        await setDoc(doc(db, 'rewards', payment.userId), {
          userId: payment.userId,
          cashbackAmount: REWARD_CASHBACK,
          bonusAmount: REWARD_BONUS,
          totalAmount: REWARD_TOTAL,
          status: 'pending',
          releaseDate: rewardTs,
          releasedAt: null,
          createdAt: now,
        });
        await createNotification(payment.userId, 'reward_ready', `Your R${REWARD_TOTAL} reward is scheduled for ${formatDate(rewardDate)}.`);
      }
      await checkAndAwardPreLaunchReward(payment.userId);
    }

    await updateDoc(userRef, updates);

    if (user.referredBy) {
      await creditReferrerCommission(user.referredBy, payment.userId, payment.amount);
      await checkAndAwardPreLaunchReward(user.referredBy);
    }

    return { success: true };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Verify failed' };
  }
}

export async function updateMemberStatus(
  memberId: string,
  status: 'Active' | 'Pending' | 'Lapsed'
): Promise<{ success: boolean; error?: string }> {
  try {
    await updateDoc(doc(db, 'users', memberId), {
      isActivated: status === 'Active',
      status,
      updatedAt: serverTimestamp(),
    });
    return { success: true };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Update failed' };
  }
}

export async function recordActivationPayment(
  uid: string,
  amount: number,
  chargeId: string
): Promise<{ success: boolean; error?: string }> {
  try {
    const now = serverTimestamp();

    await addDoc(collection(db, 'payments'), {
      userId: uid,
      amount,
      type: 'self',
      status: 'paid',
      yocoChargeId: chargeId,
      createdAt: now,
      paidAt: now,
    });

    const userSnap = await getDoc(doc(db, 'users', uid));
    if (!userSnap.exists()) throw new Error('User not found');
    const user = userSnap.data() as UserData;

    const rewardDate = new Date();
    rewardDate.setDate(rewardDate.getDate() + REWARD_DELAY_WEEKS * 7);
    const coverExpiry = new Date();
    coverExpiry.setMonth(coverExpiry.getMonth() + 12);

    await updateDoc(doc(db, 'users', uid), {
      isActivated: true,
      activationDate: now,
      totalPaid: (user.totalPaid || 0) + amount,
      rewardReleaseDate: Timestamp.fromDate(rewardDate),
      funeralCoverActive: true,
      funeralCoverExpiry: Timestamp.fromDate(coverExpiry),
      updatedAt: now,
    });

    if (user.referredBy) {
      await creditReferrerCommission(user.referredBy, uid, amount);
      await checkAndAwardPreLaunchReward(user.referredBy);
    }

    await checkAndAwardPreLaunchReward(uid);

    return { success: true };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Activation failed' };
  }
}

export interface ReferralStats {
  total: number;
  paid: number;
  earnings: number;
  tier: string;
  commissionRate: number;
  nextTierAt: number | null;
}

export async function getReferralStats(uid: string): Promise<ReferralStats> {
  const [allSnap, paidSnap, userSnap] = await Promise.all([
    getDocs(query(collection(db, 'referrals'), where('referrerId', '==', uid))),
    getDocs(query(collection(db, 'referrals'), where('referrerId', '==', uid), where('status', '==', 'paid'))),
    getDoc(doc(db, 'users', uid)),
  ]);

  const total = allSnap.size;
  const paid = paidSnap.size;
  const earnings = userSnap.exists() ? ((userSnap.data().totalEarnings as number) || 0) : 0;

  let tier = 'Starter';
  let commissionRate = 0;
  let nextTierAt: number | null = 1;

  if (paid >= 20) { tier = 'Platinum'; commissionRate = 100; nextTierAt = null; }
  else if (paid >= 10) { tier = 'Gold'; commissionRate = 75; nextTierAt = 20; }
  else if (paid >= 1) { tier = 'Silver'; commissionRate = 50; nextTierAt = 10; }

  return { total, paid, earnings, tier, commissionRate, nextTierAt };
}

export async function getAllRewards(): Promise<Reward[]> {
  const snap = await getDocs(query(collection(db, 'rewards'), orderBy('createdAt', 'desc')));
  return snap.docs.map((d) => ({ id: d.id, ...d.data() } as Reward));
}

export async function getAllReferrals(): Promise<Referral[]> {
  const snap = await getDocs(query(collection(db, 'referrals'), orderBy('createdAt', 'desc')));
  return snap.docs.map((d) => ({ id: d.id, ...d.data() } as Referral));
}

// ── Withdrawals ───────────────────────────────────────────────────────────────

export async function requestWithdrawal(
  uid: string,
  userName: string,
  amount: number,
  bankDetails: { bankName: string; accountNumber: string; accountHolder: string; accountType: 'Cheque' | 'Savings' }
): Promise<{ success: boolean; error?: string }> {
  try {
    const existing = await getDocs(
      query(collection(db, 'withdrawals'), where('userId', '==', uid), where('status', '==', 'pending'), limit(1))
    );
    if (!existing.empty) return { success: false, error: 'You already have a pending withdrawal request.' };

    await addDoc(collection(db, 'withdrawals'), {
      userId: uid,
      userName,
      amount,
      ...bankDetails,
      status: 'pending',
      requestedAt: serverTimestamp(),
      processedAt: null,
      processedBy: null,
    });
    return { success: true };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Request failed' };
  }
}

export async function getUserWithdrawal(uid: string): Promise<Withdrawal | null> {
  const snap = await getDocs(
    query(collection(db, 'withdrawals'), where('userId', '==', uid), where('status', '==', 'pending'), limit(1))
  );
  if (snap.empty) return null;
  return { id: snap.docs[0].id, ...snap.docs[0].data() } as Withdrawal;
}

export async function getAllWithdrawals(): Promise<{ success: boolean; withdrawals?: Withdrawal[]; error?: string }> {
  try {
    const snap = await getDocs(query(collection(db, 'withdrawals'), orderBy('requestedAt', 'desc')));
    return { success: true, withdrawals: snap.docs.map((d) => ({ id: d.id, ...d.data() } as Withdrawal)) };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Failed' };
  }
}

export async function processWithdrawal(
  withdrawalId: string,
  action: 'approved' | 'rejected',
  adminId: string
): Promise<{ success: boolean; error?: string }> {
  try {
    const now = serverTimestamp();
    const wRef = doc(db, 'withdrawals', withdrawalId);
    const wSnap = await getDoc(wRef);
    if (!wSnap.exists()) throw new Error('Withdrawal not found');
    const w = wSnap.data() as Withdrawal;

    await updateDoc(wRef, { status: action, processedAt: now, processedBy: adminId });

    if (action === 'approved') {
      const userSnap = await getDoc(doc(db, 'users', w.userId));
      if (userSnap.exists()) {
        const currentEarnings = (userSnap.data().totalEarnings as number) || 0;
        await updateDoc(doc(db, 'users', w.userId), {
          totalEarnings: Math.max(0, currentEarnings - w.amount),
          updatedAt: now,
        });
        sendSMSNotification(
          userSnap.data().phone as string,
          `GoDirect247: Your R${w.amount} withdrawal has been approved! Funds will be transferred to your ${w.bankName} account within 1-3 business days.`
        );
      }
      await createNotification(w.userId, 'paid', `Your withdrawal of R${w.amount} was approved! Funds will be transferred to your account.`);
    } else {
      const userSnap = await getDoc(doc(db, 'users', w.userId));
      if (userSnap.exists() && userSnap.data().phone) {
        sendSMSNotification(
          userSnap.data().phone as string,
          `GoDirect247: Your R${w.amount} withdrawal was not approved. Please contact us on 078 018 7995 for assistance.`
        );
      }
      await createNotification(w.userId, 'paid', `Your withdrawal of R${w.amount} was not approved. Please contact support.`);
    }
    return { success: true };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Process failed' };
  }
}

export async function releaseReward(
  rewardId: string,
  adminId: string
): Promise<{ success: boolean; error?: string }> {
  try {
    const now = serverTimestamp();
    const rRef = doc(db, 'rewards', rewardId);
    const rSnap = await getDoc(rRef);
    if (!rSnap.exists()) throw new Error('Reward not found');
    const r = rSnap.data() as Reward;
    await updateDoc(rRef, { status: 'released', releasedAt: now, releasedBy: adminId });
    await createNotification(r.userId, 'reward_ready', `Your R${r.totalAmount} Pre-Launch Special reward has been released!`);
    return { success: true };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Release failed' };
  }
}

// ── Notifications ─────────────────────────────────────────────────────────────

export async function createNotification(
  userId: string,
  type: AppNotification['type'],
  message: string
): Promise<void> {
  await addDoc(collection(db, 'notifications'), {
    userId,
    type,
    message,
    read: false,
    createdAt: serverTimestamp(),
  });
}

export async function getUnreadNotifications(userId: string): Promise<{
  success: boolean;
  notifications?: AppNotification[];
  count?: number;
  error?: string;
}> {
  try {
    const snap = await getDocs(
      query(
        collection(db, 'notifications'),
        where('userId', '==', userId),
        where('read', '==', false),
        orderBy('createdAt', 'desc'),
        limit(20)
      )
    );
    const notifications = snap.docs.map((d) => ({ id: d.id, ...d.data() } as AppNotification));
    return { success: true, notifications, count: notifications.length };
  } catch (err) {
    return { success: false, error: err instanceof Error ? err.message : 'Failed' };
  }
}

export async function markNotificationRead(notifId: string): Promise<void> {
  await updateDoc(doc(db, 'notifications', notifId), { read: true });
}

// ── Internal helpers ──────────────────────────────────────────────────────────

async function creditReferrerCommission(
  referrerId: string,
  referredUserId: string,
  _amount: number
): Promise<void> {
  const now = serverTimestamp();
  const paidSnap = await getDocs(
    query(collection(db, 'referrals'), where('referrerId', '==', referrerId), where('status', '==', 'paid'))
  );
  const paidCount = paidSnap.size;
  const commissionAmount = getCommissionRate(paidCount + 1);

  const referralQuery = await getDocs(
    query(
      collection(db, 'referrals'),
      where('referrerId', '==', referrerId),
      where('referredUserId', '==', referredUserId),
      limit(1)
    )
  );
  if (!referralQuery.empty) {
    await updateDoc(referralQuery.docs[0].ref, { status: 'paid', commissionAmount, paidAt: now, updatedAt: now });
  }

  const referrerSnap = await getDoc(doc(db, 'users', referrerId));
  if (referrerSnap.exists()) {
    const referrerData = referrerSnap.data() as UserData;
    await updateDoc(doc(db, 'users', referrerId), {
      totalEarnings: (referrerData.totalEarnings || 0) + commissionAmount,
      updatedAt: now,
    });
    await createNotification(referrerId, 'paid', `You earned R${commissionAmount}! A referral paid their activation fee.`);
    sendSMSNotification(
      referrerData.phone as string,
      `GoDirect247: R${commissionAmount} earned! A referral just activated their policy. Log in to track your earnings.`
    );
    if (getCommissionRate(paidCount + 1) > getCommissionRate(paidCount)) {
      await createNotification(
        referrerId,
        'tier_up',
        `Commission tier increased! You now earn R${getCommissionRate(paidCount + 1)} per signup (${getTierLabel(paidCount + 1)} Tier).`
      );
      sendSMSNotification(
        referrerData.phone as string,
        `GoDirect247: You've reached ${getTierLabel(paidCount + 1)} tier! You now earn R${getCommissionRate(paidCount + 1)} per referral activation.`
      );
    }
  }
}

async function checkAndAwardPreLaunchReward(userId: string): Promise<void> {
  const existing = await getDoc(doc(db, 'rewards', userId));
  if (existing.exists()) return;

  const userSnap = await getDoc(doc(db, 'users', userId));
  if (!userSnap.exists()) return;
  const user = userSnap.data() as UserData;
  if (!user.isActivated) return;

  const paidSnap = await getDocs(
    query(collection(db, 'referrals'), where('referrerId', '==', userId), where('status', '==', 'paid'))
  );
  if (paidSnap.size < 2) return;

  const rewardDate = new Date();
  rewardDate.setDate(rewardDate.getDate() + REWARD_DELAY_WEEKS * 7);
  const now = serverTimestamp();

  await setDoc(doc(db, 'rewards', userId), {
    userId,
    cashbackAmount: REWARD_CASHBACK,
    bonusAmount: REWARD_BONUS,
    totalAmount: REWARD_TOTAL,
    status: 'pending',
    releaseDate: Timestamp.fromDate(rewardDate),
    releasedAt: null,
    preLaunchSpecial: true,
    referralCount: paidSnap.size,
    createdAt: now,
  });
  await createNotification(
    userId,
    'reward_ready',
    `Your R${REWARD_TOTAL} Pre-Launch Special reward is scheduled for ${formatDate(rewardDate)}.`
  );
}
