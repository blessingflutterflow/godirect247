/**
 * GoDirect247 Core Application Logic
 * Firebase Auth + Firestore integration
 */

// ─────────────────────────────────────────────────────────────────────────────
// FIREBASE INITIALIZATION
// ─────────────────────────────────────────────────────────────────────────────
const firebaseConfig = {
  apiKey: "AIzaSyDorSWqTXSSvF5JzmX4APRlTAMu1jYVCZs",
  authDomain: "zarkudu.firebaseapp.com",
  projectId: "zarkudu",
  storageBucket: "zarkudu.firebasestorage.app",
  messagingSenderId: "558310978632",
  appId: "1:558310978632:web:f2572a8c705f762ce9947d",
  measurementId: "G-GBJTNH9C5S"
};
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();

// ─────────────────────────────────────────────────────────────────────────────
// CONSTANTS
// ─────────────────────────────────────────────────────────────────────────────
const ACTIVATION_AMOUNT = 650;
const TOTAL_ACTIVATION = 1950; // 650 x 3
const REWARD_CASHBACK = 1950;
const REWARD_BONUS = 1050;
const REWARD_TOTAL = 3000;
const REWARD_DELAY_WEEKS = 6;
const CAMPAIGN_END_DATE = new Date('2026-05-30T23:59:59');
const FUNERAL_COVER_AMOUNT = 10000;
const FUNERAL_COVER_MONTHS = 12;

const TIER_RATES = [
  { min: 1, max: 9, rate: 50 },
  { min: 10, max: 19, rate: 75 },
  { min: 20, max: Infinity, rate: 100 }
];

// ─────────────────────────────────────────────────────────────────────────────
// HELPER FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

function generateReferralCode() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  let code = '';
  for (let i = 0; i < 8; i++) {
    code += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return code;
}

function getCommissionRate(count) {
  if (count >= 20) return TIER_RATES[2].rate;
  if (count >= 10) return TIER_RATES[1].rate;
  if (count >= 1) return TIER_RATES[0].rate;
  return 0;
}

function getTierLabel(count) {
  if (count >= 20) return 'Platinum';
  if (count >= 10) return 'Gold';
  if (count >= 1) return 'Silver';
  return 'Starter';
}

function formatCurrency(amount) {
  return 'R' + amount.toLocaleString('en-ZA');
}

function formatDate(date) {
  if (!date) return '-';
  const d = date.toDate ? date.toDate() : new Date(date);
  return d.toLocaleDateString('en-ZA', { day: '2-digit', month: 'short', year: 'numeric' });
}

function daysBetween(d1, d2) {
  const msPerDay = 1000 * 60 * 60 * 24;
  return Math.floor((d2 - d1) / msPerDay);
}

function isCampaignActive() {
  return new Date() < CAMPAIGN_END_DATE;
}

function getCampaignTimeRemaining() {
  const now = new Date();
  const diff = CAMPAIGN_END_DATE - now;
  if (diff <= 0) return { days: 0, hours: 0, minutes: 0, expired: true };
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
  return { days, hours, minutes, expired: false };
}

// ─────────────────────────────────────────────────────────────────────────────
// AUTH FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function signUpUser(email, password, userData) {
  try {
    // Check campaign expiry
    if (!isCampaignActive()) {
      throw new Error('This special offer has ended. Please contact support.');
    }

    // Create auth user
    const cred = await auth.createUserWithEmailAndPassword(email, password);
    const uid = cred.user.uid;

    // Generate unique referral code
    let referralCode = generateReferralCode();
    let exists = true;
    let attempts = 0;
    while (exists && attempts < 10) {
      const snap = await db.collection('users').where('referralCode', '==', referralCode).limit(1).get();
      exists = !snap.empty;
      if (exists) referralCode = generateReferralCode();
      attempts++;
    }

    // Get referrer from URL or localStorage
    const urlParams = new URLSearchParams(window.location.search);
    const refCode = urlParams.get('ref') || localStorage.getItem('referralCode') || null;
    let referredBy = null;

    if (refCode) {
      const referrerSnap = await db.collection('users').where('referralCode', '==', refCode).limit(1).get();
      if (!referrerSnap.empty) {
        referredBy = referrerSnap.docs[0].id;
      }
    }

    // Fraud prevention: block self-referral
    if (referredBy === uid) {
      referredBy = null;
    }

    // Build user document
    const now = firebase.firestore.FieldValue.serverTimestamp();
    const userDoc = {
      uid: uid,
      email: email,
      fullName: userData.fullName || '',
      phone: userData.phone || '',
      idNumber: userData.idNumber || '',
      employmentStatus: userData.employmentStatus || '',
      source: userData.source || '',
      planType: userData.planType || 'plus',
      tier: userData.tier || 'Silver',
      referralCode: referralCode,
      referredBy: referredBy,
      referredByName: userData.referredByName || '',
      beneficiary: userData.beneficiary || null,
      spouse: userData.spouse || null,
      dependents: userData.dependents || [],
      extendedFamily: userData.extendedFamily || null,
      isActivated: false,
      totalPaid: 0,
      activationDate: null,
      rewardReleaseDate: null,
      families: [], // 2 gift families
      funeralCoverActive: false,
      funeralCoverExpiry: null,
      applicationStatus: 'submitted',
      createdAt: now,
      updatedAt: now
    };

    await db.collection('users').doc(uid).set(userDoc);

    // Create referral record if referred by someone
    if (referredBy) {
      await db.collection('referrals').add({
        referrerId: referredBy,
        referredUserId: uid,
        referredUserName: userData.fullName || '',
        status: 'signed_up',
        commissionAmount: 0,
        paidAt: null,
        createdAt: now
      });

      // Send notification to referrer
      await createNotification(referredBy, 'joined', `${userData.fullName || 'Someone'} joined using your referral link!`);
    }

    return { success: true, uid, referralCode };
  } catch (err) {
    console.error('Sign up error:', err);
    return { success: false, error: err.message };
  }
}

async function loginUser(email, password) {
  try {
    const cred = await auth.signInWithEmailAndPassword(email, password);
    return { success: true, uid: cred.user.uid };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

async function logoutUser() {
  await auth.signOut();
  window.location.href = '../index.html';
}

async function getCurrentUser() {
  return new Promise((resolve) => {
    const unsub = auth.onAuthStateChanged((user) => {
      unsub();
      resolve(user);
    });
  });
}

async function getUserData(uid) {
  const doc = await db.collection('users').doc(uid).get();
  if (!doc.exists) return null;
  return { id: doc.id, ...doc.data() };
}

// ─────────────────────────────────────────────────────────────────────────────
// PAYMENT / ACTIVATION FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function recordPayment(userId, amount, type, familyIndex) {
  try {
    const now = firebase.firestore.FieldValue.serverTimestamp();
    const paymentRef = db.collection('payments').doc();

    await paymentRef.set({
      userId: userId,
      amount: amount,
      type: type, // 'self', 'family1', 'family2'
      familyIndex: familyIndex || null,
      status: 'pending', // admin must verify
      paidAt: null,
      verifiedBy: null,
      verifiedAt: null,
      createdAt: now
    });

    return { success: true, paymentId: paymentRef.id };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

async function verifyPayment(paymentId, adminId) {
  try {
    const now = firebase.firestore.FieldValue.serverTimestamp();
    const paymentRef = db.collection('payments').doc(paymentId);
    const paymentDoc = await paymentRef.get();

    if (!paymentDoc.exists) throw new Error('Payment not found');
    const payment = paymentDoc.data();

    await paymentRef.update({
      status: 'paid',
      verifiedBy: adminId,
      verifiedAt: now,
      paidAt: now
    });

    // Update user's total paid
    const userRef = db.collection('users').doc(payment.userId);
    const userDoc = await userRef.get();
    if (!userDoc.exists) throw new Error('User not found');
    const user = userDoc.data();

    const newTotalPaid = (user.totalPaid || 0) + payment.amount;
    const updates = {
      totalPaid: newTotalPaid,
      updatedAt: now
    };

    // Check activation: self-payment (650+) or full lump sum (1950+)
    const isSelfActivation = payment.type === 'self' && payment.amount >= ACTIVATION_AMOUNT;
    const isFullyPaid = newTotalPaid >= TOTAL_ACTIVATION && !user.isActivated;

    if ((isSelfActivation || isFullyPaid) && !user.isActivated) {
      const rewardReleaseDate = new Date();
      rewardReleaseDate.setDate(rewardReleaseDate.getDate() + (REWARD_DELAY_WEEKS * 7));

      updates.isActivated = true;
      updates.activationDate = now;
      updates.rewardReleaseDate = firebase.firestore.Timestamp.fromDate(rewardReleaseDate);
      updates.funeralCoverActive = true;
      const coverExpiry = new Date();
      coverExpiry.setMonth(coverExpiry.getMonth() + FUNERAL_COVER_MONTHS);
      updates.funeralCoverExpiry = firebase.firestore.Timestamp.fromDate(coverExpiry);

      // Standard reward only when user paid lump sum themselves
      if (isFullyPaid) {
        await db.collection('rewards').doc(payment.userId).set({
          userId: payment.userId,
          cashbackAmount: REWARD_CASHBACK,
          bonusAmount: REWARD_BONUS,
          totalAmount: REWARD_TOTAL,
          status: 'pending',
          releaseDate: updates.rewardReleaseDate,
          releasedAt: null,
          createdAt: now
        });
        await createNotification(payment.userId, 'reward_ready', `Congratulations! Your R${REWARD_TOTAL} reward is scheduled. Release date: ${formatDate(rewardReleaseDate)}`);
      }

      // Pre-Launch Special check (self activated + 2 paid referrals)
      await checkAndAwardPreLaunchReward(payment.userId);
    }

    await userRef.update(updates);

    // Credit referrer commission (only on paid referrals)
    if (user.referredBy) {
      await creditReferrerCommission(user.referredBy, payment.userId, payment.amount);
      // Check if referrer now qualifies for Pre-Launch Special reward
      await checkAndAwardPreLaunchReward(user.referredBy);
    }

    return { success: true };
  } catch (err) {
    console.error('Verify payment error:', err);
    return { success: false, error: err.message };
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// REFERRAL / COMMISSION FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function creditReferrerCommission(referrerId, referredUserId, amount) {
  try {
    const now = firebase.firestore.FieldValue.serverTimestamp();

    // Count how many PAID referrals this referrer has
    const paidReferralsSnap = await db.collection('referrals')
      .where('referrerId', '==', referrerId)
      .where('status', '==', 'paid')
      .get();

    const paidCount = paidReferralsSnap.size;
    const commissionRate = getCommissionRate(paidCount + 1); // +1 for this new one
    const commissionAmount = commissionRate;

    // Update the referral record
    const referralQuery = await db.collection('referrals')
      .where('referrerId', '==', referrerId)
      .where('referredUserId', '==', referredUserId)
      .limit(1)
      .get();

    if (!referralQuery.empty) {
      await referralQuery.docs[0].ref.update({
        status: 'paid',
        commissionAmount: commissionAmount,
        paidAt: now,
        updatedAt: now
      });
    }

    // Update referrer's earnings
    const referrerRef = db.collection('users').doc(referrerId);
    const referrerDoc = await referrerRef.get();
    if (referrerDoc.exists) {
      const currentEarnings = referrerDoc.data().totalEarnings || 0;
      await referrerRef.update({
        totalEarnings: currentEarnings + commissionAmount,
        updatedAt: now
      });

      // Notify referrer
      const newPaidCount = paidCount + 1;
      const newRate = getCommissionRate(newPaidCount);
      const oldRate = getCommissionRate(paidCount);

      await createNotification(referrerId, 'paid', `You earned R${commissionAmount}! ${referrerDoc.data().fullName || 'A referral'} paid their activation fee.`);

      // Tier up notification
      if (newRate > oldRate) {
        await createNotification(referrerId, 'tier_up', `Commission tier increased! You now earn R${newRate} per signup (${getTierLabel(newPaidCount)} Tier).`);
      }
    }

    return { success: true };
  } catch (err) {
    console.error('Credit commission error:', err);
    return { success: false, error: err.message };
  }
}

async function getReferralStats(userId) {
  try {
    const referralsSnap = await db.collection('referrals')
      .where('referrerId', '==', userId)
      .get();

    let totalReferrals = 0;
    let paidReferrals = 0;
    let totalEarnings = 0;
    const referrals = [];

    referralsSnap.forEach((doc) => {
      const r = doc.data();
      totalReferrals++;
      if (r.status === 'paid') {
        paidReferrals++;
        totalEarnings += (r.commissionAmount || 0);
      }
      referrals.push({ id: doc.id, ...r });
    });

    const currentRate = getCommissionRate(paidReferrals);
    const tierLabel = getTierLabel(paidReferrals);
    const nextTier = paidReferrals < 10 ? 10 : paidReferrals < 20 ? 20 : null;
    const progressToNext = nextTier ? paidReferrals : null;

    return {
      success: true,
      totalReferrals,
      paidReferrals,
      totalEarnings,
      currentRate,
      tierLabel,
      nextTier,
      progressToNext,
      referrals
    };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// NOTIFICATION FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function createNotification(userId, type, message) {
  try {
    const now = firebase.firestore.FieldValue.serverTimestamp();
    await db.collection('notifications').add({
      userId: userId,
      type: type, // 'joined', 'paid', 'tier_up', 'reward_ready'
      message: message,
      read: false,
      createdAt: now
    });
    return { success: true };
  } catch (err) {
    console.error('Create notification error:', err);
    return { success: false };
  }
}

async function getUnreadNotifications(userId) {
  try {
    const snap = await db.collection('notifications')
      .where('userId', '==', userId)
      .where('read', '==', false)
      .orderBy('createdAt', 'desc')
      .limit(20)
      .get();

    const notifications = [];
    snap.forEach((doc) => {
      notifications.push({ id: doc.id, ...doc.data() });
    });
    return { success: true, notifications, count: notifications.length };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

async function markNotificationRead(notifId) {
  try {
    await db.collection('notifications').doc(notifId).update({ read: true });
    return { success: true };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// ADMIN FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function isAdmin(uid) {
  try {
    const doc = await db.collection('admins').doc(uid).get();
    return doc.exists;
  } catch (err) {
    return false;
  }
}

async function getAllMembers() {
  try {
    const snap = await db.collection('users').orderBy('createdAt', 'desc').get();
    const members = [];
    snap.forEach((doc) => {
      members.push({ id: doc.id, ...doc.data() });
    });
    return { success: true, members };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

async function getPendingPayments() {
  try {
    const snap = await db.collection('payments')
      .where('status', '==', 'pending')
      .orderBy('createdAt', 'desc')
      .get();
    const payments = [];
    snap.forEach((doc) => {
      payments.push({ id: doc.id, ...doc.data() });
    });
    return { success: true, payments };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

async function getDashboardStats() {
  try {
    const usersSnap = await db.collection('users').get();
    const paymentsSnap = await db.collection('payments').where('status', '==', 'paid').get();
    const pendingSnap = await db.collection('payments').where('status', '==', 'pending').get();

    let totalMembers = 0;
    let activePolicies = 0;
    let totalRevenue = 0;

    usersSnap.forEach((doc) => {
      totalMembers++;
      const u = doc.data();
      if (u.isActivated) activePolicies++;
    });

    paymentsSnap.forEach((doc) => {
      totalRevenue += doc.data().amount || 0;
    });

    return {
      success: true,
      totalMembers,
      activePolicies,
      pendingPayments: pendingSnap.size,
      totalRevenue
    };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// FAMILY / GIFT FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function addFamilyMember(userId, familyData) {
  try {
    const userRef = db.collection('users').doc(userId);
    const userDoc = await userRef.get();
    if (!userDoc.exists) throw new Error('User not found');

    const families = userDoc.data().families || [];
    if (families.length >= 2) {
      throw new Error('You can only gift 2 families');
    }

    families.push({
      fullName: familyData.fullName,
      phone: familyData.phone,
      idNumber: familyData.idNumber,
      relationship: familyData.relationship || 'family',
      addedAt: firebase.firestore.FieldValue.serverTimestamp()
    });

    await userRef.update({
      families: families,
      updatedAt: firebase.firestore.FieldValue.serverTimestamp()
    });

    return { success: true };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// REWARD FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

async function checkAndAwardPreLaunchReward(userId) {
  try {
    const now = firebase.firestore.FieldValue.serverTimestamp();

    // Prevent duplicate reward
    const existingReward = await db.collection('rewards').doc(userId).get();
    if (existingReward.exists) return { success: true, alreadyAwarded: true };

    // Get user
    const userRef = db.collection('users').doc(userId);
    const userDoc = await userRef.get();
    if (!userDoc.exists) return { success: false, error: 'User not found' };
    const user = userDoc.data();

    // Must be activated themselves
    if (!user.isActivated) return { success: true, notYet: true, reason: 'User not activated' };

    // Must have at least 2 paid referrals
    const paidReferralsSnap = await db.collection('referrals')
      .where('referrerId', '==', userId)
      .where('status', '==', 'paid')
      .get();

    if (paidReferralsSnap.size < 2) return { success: true, notYet: true, reason: `Only ${paidReferralsSnap.size} paid referrals` };

    // All conditions met — create reward
    const rewardReleaseDate = new Date();
    rewardReleaseDate.setDate(rewardReleaseDate.getDate() + (REWARD_DELAY_WEEKS * 7));

    await db.collection('rewards').doc(userId).set({
      userId: userId,
      cashbackAmount: REWARD_CASHBACK,
      bonusAmount: REWARD_BONUS,
      totalAmount: REWARD_TOTAL,
      status: 'pending',
      releaseDate: firebase.firestore.Timestamp.fromDate(rewardReleaseDate),
      releasedAt: null,
      preLaunchSpecial: true,
      referralCount: paidReferralsSnap.size,
      createdAt: now
    });

    await createNotification(userId, 'reward_ready', `Congratulations! Your R${REWARD_TOTAL} Pre-Launch Special reward is scheduled. Release date: ${formatDate(rewardReleaseDate)}. You recruited ${paidReferralsSnap.size} families plus your own activation!`);

    return { success: true, awarded: true };
  } catch (err) {
    console.error('Pre-launch reward check error:', err);
    return { success: false, error: err.message };
  }
}

async function getUserReward(userId) {
  try {
    const doc = await db.collection('rewards').doc(userId).get();
    if (!doc.exists) return { success: true, reward: null };
    return { success: true, reward: { id: doc.id, ...doc.data() } };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

async function releaseReward(userId) {
  try {
    const now = firebase.firestore.FieldValue.serverTimestamp();
    await db.collection('rewards').doc(userId).update({
      status: 'released',
      releasedAt: now
    });
    return { success: true };
  } catch (err) {
    return { success: false, error: err.message };
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// CAMPAIGN FUNCTIONS
// ─────────────────────────────────────────────────────────────────────────────

function getCampaignStatus() {
  const remaining = getCampaignTimeRemaining();
  return {
    active: isCampaignActive(),
    ...remaining,
    endDate: formatDate(CAMPAIGN_END_DATE)
  };
}

// ─────────────────────────────────────────────────────────────────────────────
// UI HELPERS
// ─────────────────────────────────────────────────────────────────────────────

function showToast(message, type = 'info') {
  const toast = document.createElement('div');
  toast.className = `fixed bottom-5 right-5 z-50 px-5 py-3 rounded-xl text-sm font-medium animate-bounce ${
    type === 'success' ? 'bg-teal text-white' :
    type === 'error' ? 'bg-danger text-white' :
    'bg-gold text-dark'
  }`;
  toast.textContent = message;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 4000);
}

function showLoading(el, text = 'Loading...') {
  if (typeof el === 'string') el = document.querySelector(el);
  if (el) {
    el.dataset.originalText = el.textContent;
    el.textContent = text;
    el.disabled = true;
  }
}

function hideLoading(el) {
  if (typeof el === 'string') el = document.querySelector(el);
  if (el) {
    el.textContent = el.dataset.originalText || el.textContent;
    el.disabled = false;
  }
}

// ─────────────────────────────────────────────────────────────────────────────
// EXPORTS (for use in page-specific scripts)
// ─────────────────────────────────────────────────────────────────────────────
// All functions above are globally available since this is loaded as a script.
