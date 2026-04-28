'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { loginUser } from '@/lib/firebase-service';

export default function LoginPage() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault();
    setError('');
    setLoading(true);
    const result = await loginUser(email, password);
    setLoading(false);
    if (result.success) {
      router.push('/dashboard');
    } else {
      setError(result.error || 'Login failed. Please try again.');
    }
  }

  return (
    <div className="min-h-screen bg-[#191c1f] flex items-center justify-center px-5">
      <div className="w-full max-w-sm">
        <div className="text-center mb-10 ani1">
          <Link href="/" className="font-display font-extrabold text-white text-2xl mb-1 inline-block">
            Go<span className="text-[#f3cc20]">Direct</span>247
          </Link>
          <p className="text-white/40 text-sm mt-1">Sign in to your dashboard</p>
        </div>

        <form
          onSubmit={handleLogin}
          className="ani2 bg-white/[0.06] border border-white/10 rounded-2xl p-7"
        >
          <h1 className="font-display font-extrabold text-white text-xl mb-6">Sign in</h1>
          <div className="space-y-4 mb-6">
            <div>
              <label className="text-white/50 text-xs font-semibold uppercase tracking-wide block mb-2">
                Email
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@example.com"
                required
                className="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm"
              />
            </div>
            <div>
              <label className="text-white/50 text-xs font-semibold uppercase tracking-wide block mb-2">
                Password
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="••••••••"
                required
                className="w-full bg-white/10 border border-white/15 rounded-xl px-4 py-3.5 text-white placeholder-white/30 text-sm"
              />
            </div>
          </div>

          {error && <p className="text-[#e23b4a] text-xs text-center mb-4">{error}</p>}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-[#f3cc20] text-[#191c1f] font-display font-bold py-4 rounded-full hover:bg-[#c9a800] transition-all text-sm disabled:opacity-60"
          >
            {loading ? 'Signing in…' : 'Sign in'}
          </button>
        </form>

        <p className="text-center text-white/30 text-xs mt-6">
          <Link href="/" className="hover:text-white/60 transition-colors">
            Back to website
          </Link>
          {' · '}
          <Link href="/signup" className="hover:text-white/60 transition-colors">
            Create account
          </Link>
        </p>
      </div>
    </div>
  );
}
