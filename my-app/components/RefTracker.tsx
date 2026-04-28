'use client';

import { useEffect } from 'react';

export function RefTracker({ code }: { code?: string }) {
  useEffect(() => {
    if (code) localStorage.setItem('referralCode', code);
  }, [code]);
  return null;
}
