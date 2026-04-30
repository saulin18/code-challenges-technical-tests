import { NextRequest, NextResponse } from "next/server";
import { cookies } from "next/headers";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const code = searchParams.get("code");
  const state = searchParams.get("state");

  if (!code || !state) {
    return NextResponse.json(
      { error: "Missing code or state" },
      { status: 400 },
    );
  }

  const cookieStore = await cookies();
  const savedState = cookieStore.get("google_state")?.value;

  if (savedState !== state) {
    return NextResponse.json({ error: "Invalid state" }, { status: 400 });
  }

  const verifier = cookieStore.get("google_verifier")?.value;

  if (!verifier) {
    return NextResponse.json({ error: "Missing verifier" }, { status: 400 });
  }

  const tokenResponse = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: new URLSearchParams({
      code,
      client_id: process.env.GOOGLE_CLIENT_ID!,
      client_secret: process.env.GOOGLE_CLIENT_SECRET!,
      redirect_uri: "http://localhost:3000/api/auth/callback/google",
      code_verifier: verifier,
      grant_type: "authorization_code",
    }).toString(),
  });

  const data = await tokenResponse.json();

  if (!data.access_token) {
    return NextResponse.json(
      { error: "Failed to get access token" },
      { status: 400 },
    );
  }

  const userResponse = await fetch(
    "https://www.googleapis.com/oauth2/v1/userinfo",
    {
      headers: {
        Authorization: `Bearer ${data.access_token}`,
      },
    },
  );

  if(!userResponse.ok) {

    return NextResponse.json({ error: "Failed to get user profile" }, { status: 400 });

  }

  const user = await userResponse.json();

  return NextResponse.json({ data: user });
}
