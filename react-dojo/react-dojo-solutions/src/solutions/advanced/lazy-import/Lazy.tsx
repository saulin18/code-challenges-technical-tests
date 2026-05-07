import { useState, Suspense } from "react";
// TODO: importa EditorModal con lazy() + setTimeout para simular latencia
import { lazy } from "react";
const EditorModal = lazy(() => import("./Editor"));
export default function LazyImport() {
  const [open, setOpen] = useState(false);

  return (
    <div style={{ padding: 24, fontFamily: "system-ui" }}>
      <p style={{ color: "var(--fg-muted)" }}>
        El editor pesa. Solo descárgalo al abrir.
      </p>
      <button onClick={() => setOpen(true)}>abrir editor</button>

      {/* TODO: monta el modal solo si open, envuelto en Suspense */}
      {open && (
        <div style={{ marginTop: 16 }}>
          <Suspense fallback={<div>cargando...</div>}>
            <EditorModal onClose={() => setOpen(false)} />
          </Suspense>
        </div>
      )}
    </div>
  );
}
