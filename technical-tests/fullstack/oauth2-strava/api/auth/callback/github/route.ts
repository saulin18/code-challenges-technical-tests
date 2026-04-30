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
  const savedState = cookieStore.get("github_oauth_state")?.value;


  if (savedState !== state) {
    return NextResponse.json({ error: "Invalid state" }, { status: 400 });
  }

  const tokenResponse = await fetch("https://github.com/login/oauth/access_token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json",
    },
    body:  JSON.stringify({
      code,
      client_id: process.env.GITHUB_CLIENT_ID,
      client_secret: process.env.GITHUB_CLIENT_SECRET,
      redirect_uri: "http://localhost:3000/api/auth/callback/github"
    }),
  });

  const data = await tokenResponse.json();

  if(!data.access_token) {
    return NextResponse.json({ error: "Failed to get access token" }, { status: 400 });
  }

  const githubResponse = await fetch("https://api.github.com/user", {
    headers: {
        Authorization: `Bearer ${data.access_token}`
    }},
  );

  if(!githubResponse.ok) {
    return NextResponse.json({ error: "Failed to get user profile" }, { status: 400 });
  }
  const profile = await githubResponse.json();

  return NextResponse.json({ data: profile });
}
