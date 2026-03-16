import { createContext, useContext, useState } from "react";
import type { SidebarItem } from "@/features/chat/components/sidebar-chat";
import { useRooms } from "@/features/chat/hooks/useRooms";

export const useSidebar = () => {
  return useContext(SidebarContext);
};

export type SidebarContextType = {
  items: SidebarItem[];
  isOpen: boolean;
  setIsOpen: (isOpen: boolean) => void;
};

export const SidebarContext = createContext<SidebarContextType | null>(null);

export const SidebarProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [isOpen, setIsOpen] = useState(true);
  const { sidebarItemsArr } = useRooms();

  const value: SidebarContextType = {
    items: sidebarItemsArr,
    isOpen,
    setIsOpen,
  };

  return (
    <SidebarContext.Provider value={value}>{children}</SidebarContext.Provider>
  );
};
