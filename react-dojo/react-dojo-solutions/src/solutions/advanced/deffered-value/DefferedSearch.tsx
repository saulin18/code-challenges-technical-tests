import { useState, useMemo, useDeferredValue } from "react";

function HeavyList({ query }: { query: string }) {
  const items = useMemo(() => {
    const result = [];
    for (let i = 0; i < 6000; i++) {
      const s = "row " + i;
      if (s.includes(query)) result.push(s);
    }
    // trabajo extra para hacerlo notoriamente lento
    let x = 0;
    for (let i = 0; i < 80_000; i++) x += i;
    return result;
  }, [query]);

  return (
    <ul
      style={{
        height: 200,
        overflow: "auto",
        margin: 0,
        padding: "0 0 0 16px",
      }}
    >
      {items.slice(0, 200).map((it) => (
        <li key={it}>{it}</li>
      ))}
    </ul>
  );
}

export default function DefferedSearch() {
  const [query, setQuery] = useState("");

  // TODO: crea 'deferred' a partir de query con useDeferredValue
  // TODO: 'stale' = query !== deferred
  const deferred = useDeferredValue(query);
  return (
    <div style={{ padding: 24, fontFamily: "system-ui" }}>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="escribe para filtrar..."
        style={{ width: "100%" }}
      />
      <p
        style={{
          color: "var(--fg-muted)",
          fontSize: 12,
          fontFamily: "monospace",
        }}
      >
        {/* muestra 'actualizando...' cuando stale, o 'al día' */}
        {query !== deferred ? "actualizando..." : "al día"}
      </p>
      <div>
        {/* TODO: atenúa con opacity cuando stale; pasa 'deferred' a HeavyList */}
        <HeavyList query={deferred} />
      </div>
    </div>
  );
}
