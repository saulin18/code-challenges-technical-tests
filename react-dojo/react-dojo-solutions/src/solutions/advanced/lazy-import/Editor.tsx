import { useState } from "react";

export default function EditorModal({ onClose }: { onClose: () => void }) {
  const [text, setText] = useState("escribe algo pesado...");
  return (
    <div style={{
      padding: 16, border: "1px solid var(--line-strong)", borderRadius: 4,
      background: "var(--surface-1)"
    }}>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={5}
        style={{ width: "100%", fontFamily: "ui-monospace, monospace" }}
      />
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 8 }}>
        <small style={{ color: "var(--fg-muted)" }}>
          {text.length} caracteres
        </small>
        <button onClick={onClose}>cerrar</button>
      </div>
    </div>
  );
}
