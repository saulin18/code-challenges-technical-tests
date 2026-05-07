import { useActionState } from "react";

type State = {
  error?: string;
  ok?: boolean;
  username?: string;
};

async function registerAction(
  prevState: State,
  formData: FormData,
): Promise<State> {
  const username = formData.get("username")?.toString().trim();
  const email = formData.get("email")?.toString().trim();

  if (!username || username.length < 3) {
    return { error: "Username: mínimo 3 caracteres." };
  }

  if (!email || !email.includes("@")) {
    return { error: "Email inválido." };
  }

  return { ok: true, username };
}

export default function FormActionState() {
  const [state, formAction, isPending] = useActionState(registerAction, null);

  if (state?.ok) {
    return (
      <div style={{ padding: 24 }}>
        <p>
          ✅ Bienvenido, <strong>@{state.username}</strong>!
        </p>
      </div>
    );
  }

  return (
    <div style={{ padding: 24, maxWidth: 300 }}>
      <h3 style={{ margin: "0 0 16px", fontSize: 15 }}>Crear cuenta</h3>

      <form
        action={formAction}
        style={{ display: "flex", flexDirection: "column", gap: 10 }}
      >
        <input name="username" placeholder="Usuario" disabled={isPending} />
        <input name="email" placeholder="Email" disabled={isPending} />
        {state?.error && (
          <p style={{ color: "#c87474", fontSize: 12, margin: 0 }}>
            {state.error}
          </p>
        )}
        <button type="submit" disabled={isPending}>
          {isPending ? "Registrando..." : "Registrarse"}
        </button>
      </form>
    </div>
  );
}
