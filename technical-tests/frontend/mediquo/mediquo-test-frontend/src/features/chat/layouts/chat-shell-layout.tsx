import { Outlet } from "react-router-dom";
import SidebarChat from "@/features/chat/components/sidebar-chat";


export function ChatShellLayout() {
  return (
    <div className="flex bg-background h-dvh w-full">
      <SidebarChat />
      <section className="flex min-w-0 flex-1 flex-col">
        <Outlet />
      </section>
    </div>
  );
}
