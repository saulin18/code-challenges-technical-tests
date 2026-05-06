import React from "react";

interface InputProps extends React.HTMLAttributes<HTMLInputElement> {
  text: string;
  setText: (text: string) => void;
  doManualFocus: () => void;
  ref: React.Ref<HTMLInputElement>;
  renderCounter?: number;
}

const Input: React.FC<InputProps> = ({ text, setText, doManualFocus, ref, renderCounter }) => {
  return (
    <div style={{ padding: 24, fontFamily: "system-ui" }}>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="escribe algo..."
        style={{ width: "100%" }}
        ref={ref}
      />
      <div style={{ display: "flex", gap: 8, marginTop: 12 }}>
        <button onClick={() => doManualFocus()}>Enfocar</button>
        <button onClick={() => setText("")}>Limpiar</button>
      </div>
      <p
        style={{
          marginTop: 12,
          color: "var(--fg-muted)",
          fontFamily: "monospace",
        }}
      >
        renders: {renderCounter} · texto: "{text}"
      </p>
    </div>
  );
};

export default Input;
