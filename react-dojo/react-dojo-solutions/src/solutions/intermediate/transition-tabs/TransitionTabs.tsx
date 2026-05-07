import { useState, useTransition } from "react";

function SlowTab() {
  // renderiza 4000 items intencionalmente lento
  const items = [];
  for (let i = 0; i < 4000; i++) {
    items.push(
      <li key={i} style={{ padding: "1px 0", fontSize: 12 }}>
        item {i}
      </li>,
    );
  }
  return (
    <ul
      style={{
        height: 200,
        overflow: "auto",
        padding: "0 0 0 16px",
        margin: 0,
      }}
    >
      {items}
    </ul>
  );
}

const TABS = ["inicio", "lista lenta", "ajustes"];

export default function TransitionTabs() {
  const [activeTab, setActiveTab] = useState("inicio");
  // TODO: usa useTransition para envolver setActiveTab
  // TODO: usa isPending para mostrar feedback visual
  const [isPending, startTransition] = useTransition();
  return (
    <div style={{ padding: 24 }}>
      <div style={{ display: "flex", gap: 4, marginBottom: 16 }}>
        {TABS.map((tab) => (
          <button
            key={tab}
            onClick={() => startTransition(() => setActiveTab(tab))} // TODO: envolver en startTransition
            style={{
              fontWeight: activeTab === tab ? "bold" : "normal",
              // TODO: atenúa con opacity cuando isPending y tab !== activeTab
              opacity: isPending && activeTab !== tab ? 0.5 : 1,
            }}
          >
            {tab}
          </button>
        ))}
      </div>
      <div>
        {activeTab === "inicio" && <p>Bienvenido a inicio.</p>}
        {activeTab === "lista lenta" && <SlowTab />}
        {activeTab === "ajustes" && <p>Ajustes de la app.</p>}
      </div>
    </div>
  );
}
