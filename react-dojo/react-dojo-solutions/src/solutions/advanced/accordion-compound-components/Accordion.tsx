import {
  useState,
  useContext,
  createContext,
  useMemo,
  useCallback,
} from "react";
import type React from "react";
import type { ReactNode } from "react";
// Accordion con props — refactoriza al patrón Compound Components
const AccordionContext = createContext<{
  activeId: string | null;
  toggle: (id: string) => void;
}>({ activeId: null, toggle: () => {} });

const AccordionProvider = ({ children }: { children: ReactNode }) => {
  const [activeId, setActiveId] = useState<string | null>(null);
  const toggle = useCallback(
    (id: string) => setActiveId((prev) => (prev === id ? null : id)),
    [],
  );

  const value = useMemo(() => ({ activeId, toggle }), [activeId, toggle]);
  return (
    <AccordionContext.Provider value={value}>
      {children}
    </AccordionContext.Provider>
  );
};

function Accordion({ items }: { items: Item[] }) {
  return (
    <AccordionProvider>
      <div style={{ fontFamily: "system-ui", maxWidth: 480 }}>
        {items.map((item) => (
          <AccordionItem key={item.id} item={item}>
            {item.content}
          </AccordionItem>
        ))}
      </div>
    </AccordionProvider>
  );
}

type accordionItemContextType = {
  id: string;
};

const AccordionItemContext = createContext<accordionItemContextType | null>(
  null,
);

const AccordionItemProvider = ({ children, id }: { children: ReactNode, id: string }) => {
  return (
    <AccordionItemContext.Provider value={{ id }}>
      {children}
    </AccordionItemContext.Provider>
  );
};

function AccordionTrigger({ children }: { children: ReactNode }) {
  const { id } = useContext(AccordionItemContext);
  const { toggle, activeId } = useContext(AccordionContext);
  return (
    <button
      onClick={() => toggle && toggle(id)}
      style={{
        width: "100%",
        textAlign: "left",
        padding: "12px 8px",
        background: "transparent",
        border: "none",
        cursor: "pointer",
        fontWeight: 600,
        fontSize: 15,
        color: "var(--fg)",
        display: "flex",
        justifyContent: "space-between",
      }}
    >
      {children}
      <span>{activeId === id ? "▲" : "▼"}</span>
    </button>
  );
}

function AccordionItem({
  children,
  item,
}: {
  children: ReactNode;
  item: Item;
}) {
  const { activeId } = useContext(AccordionContext);
  return (
    <AccordionItemProvider id={item.id}>
      <div
        key={item.id}
        style={{ borderBottom: "1px solid var(--line-strong)" }}
      >
        <AccordionTrigger>{item.title}</AccordionTrigger>
        {activeId === item.id && (
          <p
            style={{
              margin: 0,
              padding: "0 8px 12px",
              color: "var(--fg-muted)",
              fontSize: 14,
            }}
          >
            {children}
          </p>
        )}
      </div>
    </AccordionItemProvider>
  );
}

type Item = {
  id: string;
  title: string;
  content: string;
};

const items: Item[] = [
  {
    id: "1",
    title: "¿Qué es React?",
    content:
      "Una librería de JavaScript para construir interfaces de usuario basadas en componentes.",
  },
  {
    id: "2",
    title: "¿Qué es un hook?",
    content:
      "Una función que empieza por 'use' y permite usar características de React desde componentes funcionales.",
  },
  {
    id: "3",
    title: "¿Qué es el Virtual DOM?",
    content:
      "Una representación en memoria del DOM real que React usa para calcular el mínimo de cambios necesarios.",
  },
];

export default function AccordionRender() {
  return <Accordion items={items} />;
}
