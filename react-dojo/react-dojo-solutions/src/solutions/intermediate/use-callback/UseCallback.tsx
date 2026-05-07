import { useState, useCallback, memo } from "react";

type ItemProps = {
  name: string;
  onDelete: (name: string) => void;
};

const Item = memo(function Item({ name, onDelete }: ItemProps) {
  console.log("render:", name); // observa cuántos renders hay
  return (
    <li
      style={{
        display: "flex",
        gap: 8,
        alignItems: "center",
        padding: "4px 0",
      }}
    >
      <span>{name}</span>
      <button onClick={() => onDelete(name)}>×</button>
    </li>
  );
});

const ITEMS = ["manzana", "banana", "cereza", "durazno", "higo"];

export default function App() {
  const [items, setItems] = useState<string[]>(ITEMS);
  const [count, setCount] = useState<number>(0);

  // TODO: envuelve en useCallback para que memo(Item) funcione
  const onDelete = useCallback(
    (name: string) => setItems((prev) => prev.filter((i) => i !== name)),
    [],
  );

  return (
    <div style={{ padding: 24 }}>
      <p style={{ fontSize: 12, color: "var(--fg-muted)", marginBottom: 12 }}>
        Abre la consola y presiona el contador — observa los re-renders
      </p>
      <button
        onClick={() => setCount((c) => c + 1)}
        style={{ marginBottom: 16 }}
      >
        contador: {count}
      </button>
      <ul style={{ listStyle: "none", padding: 0 }}>
        {items.map((name) => (
          <Item key={name} name={name} onDelete={onDelete} />
        ))}
      </ul>
    </div>
  );
}
