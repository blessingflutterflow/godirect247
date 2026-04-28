import { NextRequest, NextResponse } from 'next/server';

function normalizePhone(phone: string): string {
  const digits = phone.replace(/\D/g, '');
  if (digits.startsWith('0') && digits.length === 10) return `+27${digits.slice(1)}`;
  if (digits.startsWith('27') && digits.length === 11) return `+${digits}`;
  return `+${digits}`;
}

export async function POST(request: NextRequest) {
  try {
    const { phone, code } = await request.json();
    if (!phone || !code) return NextResponse.json({ error: 'Phone and code required' }, { status: 400 });

    const sid = process.env.TWILIO_ACCOUNT_SID;
    const token = process.env.TWILIO_AUTH_TOKEN;
    const serviceSid = process.env.TWILIO_VERIFY_SERVICE_SID;

    if (!sid || !token || !serviceSid || serviceSid.startsWith('VA_REPLACE')) {
      return NextResponse.json({ error: 'Verification service not configured yet' }, { status: 500 });
    }

    const to = normalizePhone(phone);
    const auth = Buffer.from(`${sid}:${token}`).toString('base64');

    const res = await fetch(
      `https://verify.twilio.com/v2/Services/${serviceSid}/VerificationCheck`,
      {
        method: 'POST',
        headers: { Authorization: `Basic ${auth}`, 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ To: to, Code: code }).toString(),
      }
    );

    const data = await res.json();

    console.log('[verify/check] to:', to, '| status:', res.status, '| twilio:', JSON.stringify(data));

    if (!res.ok) {
      return NextResponse.json(
        { valid: false, error: data.message || data.detail || 'Twilio error', twilioCode: data.code },
        { status: 400 }
      );
    }

    return NextResponse.json({ valid: data.status === 'approved', status: data.status });
  } catch {
    return NextResponse.json({ error: 'Internal error' }, { status: 500 });
  }
}
