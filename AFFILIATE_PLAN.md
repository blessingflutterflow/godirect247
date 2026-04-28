# GoDirect247 — Affiliate Marketing Feature Plan
> Status: Planning Phase | Last Updated: 27 Apr 2026

---

## 1. WHAT IS ALREADY BUILT (Backend & Partial UI)

| Feature | Status | Location |
|---------|--------|----------|
| Referral code generation on signup | ✅ Backend | `app.js` `signUpUser()` |
| `?ref=CODE` URL tracking + localStorage | ✅ Backend | `app.js` |
| Referral record in Firestore (`referrals` collection) | ✅ Backend | `app.js` |
| Payment recording (`payments` collection, pending → admin verify) | ✅ Backend | `app.js` `recordPayment()` |
| Admin payment verification + user activation | ✅ Backend | `app.js` `verifyPayment()` |
| Tiered commission logic (R50 / R75 / R100) | ✅ Backend | `app.js` `getCommissionRate()` |
| Pre-Launch Special reward check (self-activated + 2 paid referrals = R3,000) | ✅ Backend | `app.js` `checkAndAwardPreLaunchReward()` |
| Notification creation (joined / paid / tier_up / reward_ready) | ✅ Backend | `app.js` `createNotification()` |
| Bell icon + dropdown on user dashboard | ✅ UI | `dashboard/index.html` |
| Pre-Launch Special banner on landing page | ✅ UI | `index.html` |
| Pre-Launch Special banner on signup page | ✅ UI | `signup/index.html` |
| Admin dashboard — Members / Payments / Rewards / Referrals tabs | ✅ UI | `admin/dashboard.html` |

---

## 2. WHAT IS MISSING (Requires Planning & Implementation)

### A. USER-FACING REFERRAL HUB
**Problem:** A logged-in user has NO way to see their referral link, copy it, or track progress.

**Questions for Client:**
1. Where should the referral hub live? 
   - Option A: New tab/section inside existing `dashboard/index.html`
   - Option B: Dedicated page `dashboard/referrals.html`
2. What sharing methods?
   - Copy link button
   - WhatsApp share button
   - SMS share button
   - Email share button
   - All of the above?

**Proposed UI Elements:**
- **Referral Link Box:** Display `https://godirect247.co.za/signup?ref=ABCDEF12` with Copy button
- **Stats Cards:** Total Referrals | Paid Referrals | Total Earnings | Current Tier (Silver/Gold/Platinum)
- **Tier Progress Bar:** "7 of 10 to Gold Tier (R75)" — visual bar
- **Referral List Table:** Name | Status (signed up / paid) | Commission Earned | Date
- **Earnings History:** Mini table of each commission credit

---

### B. PRE-LAUNCH SPECIAL PROGRESS TRACKER
**Problem:** User cannot see how close they are to the R3,000 reward.

**Current Logic:**
- User pays R650 → activated
- 2 referred families pay R650 each → R3,000 reward unlocked
- Reward released after 6 weeks

**Proposed UI Elements:**
- **3-Step Visual Tracker:**
  - Step 1: ✅ You activated (R650 paid) — OR — ⏳ Pending verification
  - Step 2: Family 1 activated (0/1) — shows name/phone if referred
  - Step 3: Family 2 activated (0/1) — shows name/phone if referred
- **Reward Status Card:**
  - "R3,000 Reward: LOCKED / PENDING / RELEASED"
  - Countdown: "Releases in 14 days" (if pending)
  - "Released on 15 June 2026" (if scheduled)
- **Funeral Cover Badge:** "R10,000 Cover Active — Expires 27 Apr 2027"

**Open Question:** Where does this live?
- Inside main dashboard as a new card?
- Inside the referral hub?
- Both?

---

### C. PAYMENT / ACTIVATION FLOW
**Problem:** Users sign up but there's NO UI to actually pay the R650.

**What exists:** `recordPayment()` creates a pending payment doc. Admin verifies it.

**Missing:**
- User dashboard needs a "Pay Activation Fee" section
- Bank details display (which bank account? reference number?)
- Proof-of-payment upload (screenshot/photo of EFT)
- Payment status tracker (Pending → Verified)

**Questions for Client:**
1. What bank account details should be shown to users for EFT?
2. Do users upload proof-of-payment, or does admin mark it paid manually?
3. Is there an online payment gateway (PayFast, Ozow, etc.) or only EFT?

**Proposed UI:**
- "Complete Activation" card on dashboard
- Shows bank details + auto-generated reference (e.g., `GD-ABCDEF12`)
- Upload proof-of-payment button → stores image in Firebase Storage
- Status: "Payment Pending Admin Verification"

---

### D. FAMILY GIFT / INVITATION FLOW
**Problem:** The Pre-Launch Special says "Gift 2 Families" but there's no invitation mechanism.

**Current Logic:** `addFamilyMember()` adds family data to user doc, but those families don't become separate users.

**Clarification Needed:**
Does "Gift 2 Families" mean:
- **Option A:** User adds 2 family members as dependents (no separate accounts) — ALREADY partially supported
- **Option B:** User sends a special invitation link to 2 people, who sign up as NEW users under the Pre-Launch Special — NOT built

**If Option B (recommended for tracking):**
- User generates 2 "family invitation links" from dashboard
- Each link is `signup?ref=USERCODE&family=1` and `signup?ref=USERCODE&family=2`
- When those 2 sign up and pay R650, they count toward the user's Pre-Launch reward
- Backend needs to track which referrals are "family gifts" vs regular referrals

---

### E. COMMISSION PAYOUT / WITHDRAWAL SYSTEM
**Problem:** Users earn commissions (R50/R75/R100) but cannot see or withdraw them.

**Missing:**
- User bank account details collection
- Withdrawal request flow
- Admin approval of withdrawals
- Minimum withdrawal threshold?

**Questions for Client:**
1. Is there a minimum amount before users can withdraw? (e.g., R200?)
2. How often can they withdraw? (Instant? Weekly? Monthly?)
3. Do you (admin) manually process payouts, or is there an API integration?
4. What bank details are needed? (Account number, bank name, branch code?)

**Proposed UI:**
- "Withdraw Earnings" button inside referral hub
- Form: Bank Name | Account Number | Account Type | Branch Code
- Submit → creates `withdrawals` doc (pending)
- Admin dashboard → new "Withdrawals" tab → Approve / Reject

---

### F. REWARD RELEASE MECHANISM
**Problem:** R3,000 reward is scheduled after 6 weeks, but WHO releases it?

**Current Logic:** `rewardReleaseDate` is calculated, `status: 'pending'` — but no release action.

**Questions for Client:**
1. Does the admin manually click "Release Reward" after 6 weeks?
2. Or should it auto-release (backend function checking dates daily)?
3. When released, does the user's balance update? Is there a payout flow?

**Proposed:**
- Admin dashboard → Rewards tab → "Release" button on each pending reward
- OR: Auto-release via scheduled Cloud Function (requires Firebase paid plan)
- For now: Manual admin release is simplest and safest

---

### G. NOTIFICATIONS — EXPANSION
**Already built:** Bell icon shows joined / paid / tier_up / reward_ready.

**Missing notification types:**
- `payment_verified` — "Your R650 payment was verified. You are now activated!"
- `family_joined` — "[Name] accepted your family invitation and signed up!"
- `family_paid` — "[Name] paid their activation fee. Pre-Launch reward closer!"
- `reward_released` — "Your R3,000 reward has been released!"
- `withdrawal_approved` — "Your commission withdrawal of R350 was approved."

---

### H. LANDING PAGE — REFERRAL VISITOR EXPERIENCE
**Problem:** When someone clicks a referral link, the landing page should personalize.

**Proposed:**
- Detect `?ref=CODE` on `index.html`
- Show banner: "You were invited by [Referrer Name]. Join the Pre-Launch Special!"
- Auto-pass `ref` to signup page
- Store `ref` in localStorage so it persists across page navigations

---

## 3. PROPOSED IMPLEMENTATION ORDER

| Priority | Feature | Complexity | Effort |
|----------|---------|-----------|--------|
| **P0** | Referral Hub UI on dashboard (link, stats, tier progress) | Medium | 1 session |
| **P0** | Pre-Launch Progress Tracker (3-step visual) | Medium | 1 session |
| **P1** | Payment/Activation flow (bank details + proof upload) | Medium-High | 1-2 sessions |
| **P1** | Landing page referral personalization | Low | 0.5 session |
| **P2** | Family invitation links (2 special gift links) | Medium | 1 session |
| **P2** | Withdrawal system (user request + admin approval) | Medium-High | 1-2 sessions |
| **P3** | Notification expansion (new types) | Low | 0.5 session |
| **P3** | Auto reward release (or manual admin button) | Low | 0.5 session |

---

## 4. QUESTIONS FOR CLIENT (Need Answers Before We Code)

**Please answer each with A, B, or your own answer:**

1. **Payment method:** EFT only, or do you have PayFast/Ozow integration?
2. **Family gifting:** Are the "2 families" separate accounts (Option B), or just dependents on the same account (Option A)?
3. **Withdrawals:** Minimum amount? Manual admin approval? How often?
4. **Bank details for EFT:** What account number, bank name, reference format should users use?
5. **Reward release:** Admin clicks "Release" manually, or auto-release after 6 weeks?
6. **Referral hub location:** New tab inside dashboard, or separate page?
7. **Sharing:** WhatsApp + Copy link only, or also SMS + Email?

---

## 5. TECHNICAL NOTES

- **Firebase Storage** needed for proof-of-payment uploads (free tier: 1GB)
- **Firestore indexes** needed for `referrals` queries if traffic scales
- **Security rules** must allow admin read/write on all collections; users only their own docs
- **Open rules** currently active — must lock down before launch
- **Cloud Functions** would enable auto-release, but manual is fine for MVP

---

*End of Plan. Awaiting client answers to questions in Section 4.*
