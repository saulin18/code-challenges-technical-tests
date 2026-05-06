import { useState, useMemo } from "react";

const ALL_TASKS = Array.from({ length: 500 }, (_, i) => ({
  id: i,
  text:
    ["fix bug", "write test", "review PR", "update docs", "deploy"][i % 5] +
    " #" +
    i,
  priority: ["alta", "media", "baja"][i % 3],
}));

export function UseMemoFilter() {
  const [query, setQuery] = useState("");
  const [order, setOrder] = useState("asc");
  const [count, setCount] = useState(0);

  const filtered = useMemo(() => {
    return ALL_TASKS.filter((t) => t.text.includes(query)).sort((a, b) =>
      order === "asc"
        ? a.text.localeCompare(b.text)
        : b.text.localeCompare(a.text),
    );
  }, [query, order]);

  return (
    <div style={{ padding: 24 }}>
      <p style={{ fontSize: 12, color: "var(--fg-muted)", marginBottom: 12 }}>
        Abre la consola — el contador no debería recalcular la lista
      </p>
      <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="filtrar..."
          style={{ flex: 1 }}
        />
        <select value={order} onChange={(e) => setOrder(e.target.value)}>
          <option value="asc">A → Z</option>
          <option value="desc">Z → A</option>
        </select>
      </div>
      <button
        onClick={() => setCount((c) => c + 1)}
        style={{ marginBottom: 12 }}
      >
        contador: {count}
      </button>
      <p style={{ fontSize: 12, color: "var(--fg-muted)", marginBottom: 8 }}>
        {filtered.length} tareas
      </p>
      <ul
        style={{
          listStyle: "none",
          padding: 0,
          maxHeight: 200,
          overflow: "auto",
        }}
      >
        {filtered.slice(0, 50).map((t) => (
          <li
            key={t.id}
            style={{ padding: "3px 0", fontSize: 13, display: "flex", gap: 8 }}
          >
            <span
              style={{ color: "var(--fg-muted)", fontSize: 11, minWidth: 32 }}
            >
              {t.priority}
            </span>
            <span>{t.text}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
