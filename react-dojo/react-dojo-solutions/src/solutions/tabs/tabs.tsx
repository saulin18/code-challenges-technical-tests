import { useState } from "react";

const tabs = [
  { id: "home", label: "Home", content: "Bienvenido a mi app!" },
  { id: "about", label: "About", content: "Soy desarrollador en React." },
  { id: "contact", label: "Contact", content: "contáctame@email.com" },
];

const appStyle = {
  padding: 24,
  fontFamily: "system-ui",
  background: "var(--bg)",
  minHeight: "100vh",
};

export default function App() {
  const [activateTab, setActivateTab] = useState("home");

  return (
    <div style={appStyle}>
      <p style={{ marginBottom: 24, color: "#71717a" }}>Tabs Component</p>
      <div
        style={{ display: "flex", gap: 4, borderBottom: "1px solid #3f3f46" }}
      >
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => {
              setActivateTab(tab.id);
            }}
            style={{
              padding: "8px 16px",
              backgroundColor: "transparent",
              color: "#a1a1aa",
              border: "none",
              cursor: "pointer",
            }}
          >
            {tab.label}
          </button>
        ))}
      </div>
      <div style={{ padding: 16, fontSize: 18 }}>
        {tabs.find((tab) => tab.id === activateTab)?.content}
      </div>
    </div>
  );
}
