import { createContext, useContext, useMemo, useState, memo } from "react";

type themeType = "dark" | "light";

const ThemeCtx = createContext<{
  theme: themeType;
  setTheme: (theme: (t: themeType) => themeType) => void;
} | null>(null);

function useTheme() {
  const ctx = useContext(ThemeCtx);
  if (!ctx) throw new Error("useTheme requiere ThemeProvider");
  return ctx;
}

function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<themeType>("dark");

  const value = useMemo(() => ({ theme, setTheme }), [theme, setTheme]);
  return <ThemeCtx.Provider value={value}>{children}</ThemeCtx.Provider>;
}

const Toolbar = memo(function Toolbar() {
  console.log("render Toolbar");
  const { setTheme } = useTheme();
  return (
    <button
      onClick={() =>
        setTheme((t) => (t === "dark" ? "light" : "dark"))
      }
    >
      cambiar tema
    </button>
  );
});

const Card = memo(function Card() {
  console.log("render Card");
  const { theme } = useTheme();
  return (
    <div
      style={{ padding: 12, border: "1px solid var(--line)", marginTop: 12 }}
    >
      tema: <strong>{theme}</strong>
    </div>
  );
});

export default function App() {
  const [tick, setTick] = useState(0);
  return (
    <ThemeProvider>
      <div style={{ padding: 24, fontFamily: "system-ui" }}>
        <button onClick={() => setTick((t) => t + 1)}>tick: {tick}</button>
        <Toolbar />
        <Card />
        <p style={{ color: "var(--fg-muted)", fontSize: 12, marginTop: 12 }}>
          Abre la consola: al pulsar tick, ¿se renderiza Toolbar? Memoiza el
          value.
        </p>
      </div>
    </ThemeProvider>
  );
}
