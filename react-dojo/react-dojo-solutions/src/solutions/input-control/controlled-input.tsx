import { useState } from "react";

const appStyle = {
  padding: 24,
  fontFamily: "system-ui",
  background: "var(--bg)",
  minHeight: "100vh",
};

const labelStyle = {
  marginBottom: 24,
  color: "#71717a",
};

export default function App() {
  const [text, setText] = useState("")

  return (
    <div style={appStyle}>
      <p style={labelStyle}>Input controlado</p>
      <input
        value={text} // TODO: cambia "" por text
        onChange={(e) => {
         setText(e.target.value)
        }}
        placeholder="escribe algo..."
        style={{ padding: 8, fontSize: 16, width: "100%", borderRadius: 8 }}
      />
      <p style={{ marginTop: 16, fontSize: 18 }}>
        {text}
      </p>
    </div>
  );
}
