import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const { token, amountInCents } = await request.json();

    if (!token || !amountInCents) {
      return NextResponse.json({ error: 'Missing token or amount' }, { status: 400 });
    }

    const secret = process.env.YOCO_SECRET_KEY;
    if (!secret) {
      return NextResponse.json({ error: 'Payment service not configured' }, { status: 500 });
    }

    const response = await fetch('https://online.yoco.com/v1/charges/', {
      method: 'POST',
      headers: {
        'X-Auth-Secret-Key': secret,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: new URLSearchParams({
        token,
        amountInCents: String(amountInCents),
        currency: 'ZAR',
      }).toString(),
    });

    const data = await response.json();

    if (!response.ok || data.status !== 'successful') {
      return NextResponse.json(
        { error: data.displayMessage || data.errorCode || 'Payment failed' },
        { status: 400 }
      );
    }

    return NextResponse.json({ success: true, chargeId: data.id });
  } catch {
    return NextResponse.json({ error: 'Internal error' }, { status: 500 });
  }
}
