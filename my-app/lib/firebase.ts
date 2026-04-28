import { initializeApp, getApps } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
  apiKey: "AIzaSyDorSWqTXSSvF5JzmX4APRlTAMu1jYVCZs",
  authDomain: "zarkudu.firebaseapp.com",
  projectId: "zarkudu",
  storageBucket: "zarkudu.firebasestorage.app",
  messagingSenderId: "558310978632",
  appId: "1:558310978632:web:f2572a8c705f762ce9947d",
  measurementId: "G-GBJTNH9C5S"
};

const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApps()[0];
export const auth = getAuth(app);
export const db = getFirestore(app);
export default app;
