/**
 * Seeds an admin user into Firebase Auth + Firestore.
 * Usage:
 *   node scripts/seed-admin.mjs [email] [password]
 *
 * Defaults to admin@godirect247.co.za / Admin@2026!
 */

import { initializeApp } from 'firebase/app';
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} from 'firebase/auth';
import { getFirestore, doc, setDoc, serverTimestamp } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: 'AIzaSyDorSWqTXSSvF5JzmX4APRlTAMu1jYVCZs',
  authDomain: 'zarkudu.firebaseapp.com',
  projectId: 'zarkudu',
  storageBucket: 'zarkudu.firebasestorage.app',
  messagingSenderId: '558310978632',
  appId: '1:558310978632:web:f2572a8c705f762ce9947d',
};

const ADMIN_EMAIL = process.argv[2] || 'admin@godirect247.co.za';
const ADMIN_PASSWORD = process.argv[3] || 'Admin@2026!';

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

async function seedAdmin() {
  console.log(`\nSeeding admin: ${ADMIN_EMAIL}\n`);

  let uid;

  // Try sign-in first (handles already-existing auth accounts)
  try {
    const cred = await signInWithEmailAndPassword(auth, ADMIN_EMAIL, ADMIN_PASSWORD);
    uid = cred.user.uid;
    console.log('✓ Signed in as existing user');
  } catch {
    try {
      const cred = await createUserWithEmailAndPassword(auth, ADMIN_EMAIL, ADMIN_PASSWORD);
      uid = cred.user.uid;
      console.log('✓ Created new auth user');
    } catch (err) {
      console.error('✗ Auth failed:', err.message);
      process.exit(1);
    }
  }

  // Write admin record to Firestore
  await setDoc(doc(db, 'admins', uid), {
    email: ADMIN_EMAIL,
    createdAt: serverTimestamp(),
  });

  console.log('✓ Admin record saved to Firestore (admins collection)\n');
  console.log('─────────────────────────────────────');
  console.log('  Email   :', ADMIN_EMAIL);
  console.log('  Password:', ADMIN_PASSWORD);
  console.log('  UID     :', uid);
  console.log('─────────────────────────────────────');
  console.log('\nLogin at: http://localhost:3000/admin\n');

  process.exit(0);
}

seedAdmin().catch((err) => {
  console.error(err);
  process.exit(1);
});
