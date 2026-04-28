'use client';

import { createContext, useContext, useEffect, useState, useCallback, type ReactNode } from 'react';
import { onAuthStateChanged, type User } from 'firebase/auth';
import { doc, getDoc } from 'firebase/firestore';
import { auth, db } from './firebase';
import type { UserData } from './types';

interface AuthContextType {
  user: User | null;
  userData: UserData | null;
  isAdmin: boolean;
  loading: boolean;
  refreshUserData: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType>({
  user: null,
  userData: null,
  isAdmin: false,
  loading: true,
  refreshUserData: async () => {},
});

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [userData, setUserData] = useState<UserData | null>(null);
  const [isAdmin, setIsAdmin] = useState(false);
  const [loading, setLoading] = useState(true);

  const loadUserData = useCallback(async (uid: string) => {
    try {
      const [userSnap, adminSnap] = await Promise.all([
        getDoc(doc(db, 'users', uid)),
        getDoc(doc(db, 'admins', uid)),
      ]);
      setUserData(userSnap.exists() ? ({ id: userSnap.id, ...userSnap.data() } as UserData) : null);
      setIsAdmin(adminSnap.exists());
    } catch {
      setUserData(null);
      setIsAdmin(false);
    }
  }, []);

  const refreshUserData = useCallback(async () => {
    if (user) await loadUserData(user.uid);
  }, [user, loadUserData]);

  useEffect(() => {
    const unsub = onAuthStateChanged(auth, async (u) => {
      setUser(u);
      if (u) {
        await loadUserData(u.uid);
      } else {
        setUserData(null);
        setIsAdmin(false);
      }
      setLoading(false);
    });
    return () => unsub();
  }, [loadUserData]);

  return (
    <AuthContext.Provider value={{ user, userData, isAdmin, loading, refreshUserData }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
