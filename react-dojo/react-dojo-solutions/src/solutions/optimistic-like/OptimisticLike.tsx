import { useState, useOptimistic, useTransition } from "react";

async function saveLike(liked: boolean) {
  await new Promise((r) => setTimeout(r, 800));
  if (Math.random() < 0.15) throw new Error("Error de red");
  return liked;
}

export function OptimisticLikes() {
  const [likes, setLikes] = useState(42);
  const [liked, setLiked] = useState(false);
  const [, startTransition] = useTransition();

  // TODO: crea optimisticLikes y addOptimistic con useOptimistic
  // updateFn: (currentLikes, delta) => currentLikes + delta
  const [optimisticLikes, addOptimistic] = useOptimistic(
    likes,
    (currentLikes, delta: number) => currentLikes + delta,
  );

  async function handleLike() {
    const next = !liked;
    const delta = next ? 1 : -1;
    // TODO: llama addOptimistic(delta) aquí para respuesta inmediata
    addOptimistic(delta);

    startTransition(async () => {
      try {
        await saveLike(next);
        setLikes((l) => l + delta);
        setLiked(next);
      } catch {
        // si falla, useOptimistic revierte automáticamente
      }
    });
  }

  return (
    <div style={{ padding: 24, maxWidth: 320 }}>
      <div
        style={{
          padding: 16,
          border: "1px solid var(--line)",
          borderRadius: 8,
          marginBottom: 16,
        }}
      >
        <p style={{ margin: "0 0 12px", fontSize: 14 }}>
          ¿Te gustó este artículo sobre React 19?
        </p>
        <button
          onClick={handleLike}
          style={{
            display: "flex",
            alignItems: "center",
            gap: 6,
            color: liked ? "#e0607e" : "var(--fg-muted)",
            borderColor: liked ? "#e0607e" : "var(--line-strong)",
          }}
        >
          <span>{liked ? "❤️" : "🤍"}</span>
          <span>{optimisticLikes}</span>
        </button>
      </div>
    </div>
  );
}
