import { useState } from "react";

const appStyle = {
  padding: 24,
  fontFamily: "system-ui",
  background: "var(--bg)",
  minHeight: "100vh",
};

const ToggleButton = () => {
  const [isOn, setIsOn] = useState(false);

  return (
    <div style={appStyle}>
      <p style={{ marginBottom: 24, color: "#71717a" }}>Toggle Button</p>
      <button
        onClick={() => {
          setIsOn(!isOn);
        }}
        style={{
          backgroundColor: isOn ? "#22c55e" : "#6b7280", // TODO: verde (#22c55e) cuando isOn, gris (#6b7280) cuando off
          color: "white",
          padding: "12px 24px",
          borderRadius: 8,
          border: "none",
          cursor: "pointer",
          fontSize: 18,
        }}
      >
        {isOn ? "ON" : "OFF"}
      </button>
    </div>
  );
};

export default ToggleButton;
