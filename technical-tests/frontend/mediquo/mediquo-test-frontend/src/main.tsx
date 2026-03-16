import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "@/index.css";
import App from "@/App.tsx";

const root = createRoot(document.getElementById("root") as HTMLElement);

if (!root) {
  throw new Error("Root element not found");
}

root.render(
  <StrictMode>
    <App />
  </StrictMode>,
);
