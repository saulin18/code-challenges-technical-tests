import { NextResponse } from "next/server";
import crypto from "crypto";
import { cookies } from "next/headers";

function generatePkceChallenge() {
  const verifier = crypto.randomBytes(32).toString("base64url");

  const challenge = crypto
    .createHash("sha256")
    .update(verifier)
    .digest("base64url");

  return { verifier, challenge };
}

export async function GET() {
  const state = crypto.randomBytes(32).toString("hex");

  const store = await cookies();
  store.set("google_state", state, { httpOnly: true, secure: true });

  const { verifier, challenge } = generatePkceChallenge()

  store.set("google_verifier", verifier, { httpOnly: true, secure: true });

  const params = new URLSearchParams({
    client_id: process.env.GOOGLE_CLIENT_ID!,
    redirect_uri: "http://localhost:3000/api/auth/callback/google",
    response_type: "code",
    scope: "openid profile email",
    state,
    code_challenge: challenge,
    code_challenge_method: "S256",
  });

  return NextResponse.redirect(
    new URL( 
      `https://accounts.google.com/o/oauth2/v2/auth?${params.toString()}`,
    ),
  );
}
