import { NextResponse } from "next/server";
import crypto from "crypto";
import { cookies } from "next/headers";

export async function GET() {
  const state = crypto.randomBytes(32).toString("hex");
  const cookieStore = await cookies();
  cookieStore.set("github_oauth_state", state, { httpOnly: true, secure: true, maxAge: 60 * 15, sameSite: "strict"}); // 15 minutes

  const params = new URLSearchParams({
    client_id: process.env.GITHUB_CLIENT_ID!,
    redirect_uri: "http://localhost:3000/api/auth/callback/github",
    state,
    scope: "read:user",
  });

  return NextResponse.redirect(
    new URL(
      `https://github.com/login/oauth/authorize?${params.toString()}`,
    ),
  );
}