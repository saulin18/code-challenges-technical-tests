import { useEffect, useState } from "react";

type User = {
  name: string;
  email: string;
  companyName: string;
};

type UserState = {
  user: null | User;
  loading: boolean;
  error: null | string;
};

const mapUser = (data: any): User => {
  const newUser = {
    email: data.email,
    name: data.name,
    companyName: data.company.name,
  };
  return newUser;
};

export default function FetchUsers() {
  const [userId, setUserId] = useState<number>(1);
  const [userState, setUserState] = useState<UserState>({
    user: null,
    loading: false,
    error: null,
  });

  const user = userState.user;
  const loading = userState.loading;
  const error = userState.error;

  useEffect(() => {
    const ctrl = new AbortController();
    setUserState((prev) => {
      return { ...prev, loading: true, error: null };
    });

    fetch("https://jsonplaceholder.typicode.com/users/" + userId, {
      signal: ctrl.signal,
    })
      .then((r) => r.json())
      .then((data) => {
        setUserState((prev) => {
          return { ...prev, user: mapUser(data), error: null, loading: false };
        });
      })
      .catch((err) => {
        if (err.message.includes("error: signal is aborted without reason"))
          return;
        if (err.name === "AbortError") return;
        setUserState((prev) => {
          return { ...prev, error: err.message, loading: false };
        });
      })
    return () => {
      ctrl.abort();
    };
  }, [userId]);

  return (
    <div style={{ padding: 24, fontFamily: "system-ui" }}>
      <div style={{ display: "flex", gap: 6, marginBottom: 16 }}>
        {[1, 2, 3, 4, 5].map((id) => (
          <button
            key={id}
            onClick={() => setUserId(id)}
            style={{ fontWeight: id === userId ? 700 : 400 }}
          >
            user {id}
          </button>
        ))}
      </div>
      {loading && <p style={{ color: "var(--fg-muted)" }}>cargando...</p>}
      {error && (
        <p style={{ color: "var(--error, #c98b82)" }}>error: {error}</p>
      )}
      {!loading && user && (
        <div>
          <strong>{user.name}</strong>
          <p style={{ color: "var(--fg-muted)", margin: "4px 0" }}>
            {user.email} · {user.companyName ?? ""}
          </p>
        </div>
      )}
    </div>
  );
}
