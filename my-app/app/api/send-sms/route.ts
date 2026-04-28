import { NextRequest, NextResponse } from 'next/server';

function normalizePhone(phone: string): string {
  const digits = phone.replace(/\D/g, '');
  if (digits.startsWith('0') && digits.length === 10) return `+27${digits.slice(1)}`;
  if (digits.startsWith('27') && digits.length === 11) return `+${digits}`;
  return `+${digits}`;
}

export async function POST(request: NextRequest) {
  try {
    const { to, message } = await request.json();
    if (!to || !message) return NextResponse.json({ error: 'Missing to or message' }, { status: 400 });

    const sid = process.env.TWILIO_ACCOUNT_SID;
    const token = process.env.TWILIO_AUTH_TOKEN;
    const from = process.env.TWILIO_FROM_NUMBER;

    if (!sid || !token || !from) {
      return NextResponse.json({ error: 'SMS service not configured' }, { status: 500 });
    }

    const auth = Buffer.from(`${sid}:${token}`).toString('base64');

    const res = await fetch(
      `https://api.twilio.com/2010-04-01/Accounts/${sid}/Messages.json`,
      {
        method: 'POST',
        headers: { Authorization: `Basic ${auth}`, 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ To: normalizePhone(to), From: from, Body: message }).toString(),
      }
    );

    const data = await res.json();
    if (!res.ok) return NextResponse.json({ error: data.message || 'Failed to send' }, { status: 400 });

    return NextResponse.json({ success: true, sid: data.sid });
  } catch {
    return NextResponse.json({ error: 'Internal error' }, { status: 500 });
  }
}
