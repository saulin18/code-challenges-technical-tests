import { BrowserRouter, Routes, Route } from "react-router-dom";
import { SidebarProvider } from "@/features/chat/context/sidebar-context";
import { ChatShellLayout } from "@/features/chat/layouts/chat-shell-layout";
import { ChatPage } from "@/features/chat/pages/chat-page";

function App() {
  return (
    <BrowserRouter>
      <SidebarProvider>
        <Routes>
          <Route path="/" element={<ChatShellLayout />}>
            <Route index element={<ChatPage />} />
            <Route path="rooms/:roomId" element={<ChatPage />} />
          </Route>
        </Routes>
      </SidebarProvider>
    </BrowserRouter>
  );
}

export default App;
