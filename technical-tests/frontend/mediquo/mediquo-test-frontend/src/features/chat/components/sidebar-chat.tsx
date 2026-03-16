import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import "@/index.css";
import { Input } from "@/features/shared/components/ui/input";
import { SearchIcon } from "@/features/shared/components/ui/search-icon";
import { useSidebar } from "@/features/chat/context/sidebar-context";
import {
  ExpandIcon,
  CollapseIcon,
} from "@/features/shared/components/ui/sidebar-icons";
import { extractWeekday } from "@/features/shared/utils/dates";
export type SidebarItem = {
  id: string;
  name: string;
  icon: string;
  lastMessage: string;
  lastMessageTime: string;
};

export interface SidebarChatProps extends React.HTMLAttributes<HTMLDivElement> {
  items?: SidebarItem[];
}
const SidebarChat: React.FC<SidebarChatProps> = ({
  items: itemsProp,
  ...props
}) => {
  const navigate = useNavigate();
  const { roomId } = useParams<{ roomId: string }>();
  const ctx = useSidebar();
  const items = itemsProp ?? ctx?.items ?? [];
  const { isOpen, setIsOpen } = ctx ?? {};
  
  const [searchValue, setSearchValue] = useState("");
  const filteredItems = items.filter((item) =>
    item.name.toLowerCase().includes(searchValue.toLowerCase()),
  );
  const handleSelectChat = (id: string) => {
    navigate(`/rooms/${id}`);
  };

  return (
    <div
      className={`flex shrink-0 relative transition-all duration-300 flex-col border-r
         border-border bg-background p-4 gap-4 h-full ${isOpen ? "w-[310px]" : "w-10"}`}
      {...props}
    >
      <button
        className="absolute top-4 right-4 z-30"
        onClick={() => setIsOpen?.(!isOpen)}
      >
        {isOpen ? (
          <ExpandIcon className="size-5" />
        ) : (
          <CollapseIcon className="size-5" />
        )}
      </button>

      {isOpen && (
        <>
          <Input
            className="max-w-[230px]"
            icon={<SearchIcon className="size-5" />}
            onValueChange={(value) => setSearchValue(value)}
          />

          {filteredItems.map((item: SidebarItem) => (
            <div
              key={item.id}
              className={`flex gap-4 pt-2 ${item.id === roomId ? "bg-hover" : "hover:bg-hover"}`}
              onClick={() => handleSelectChat(item.id)}
            >
              <img
                className="w-10 h-10 shrink-0 object-cover"
                src={item.icon}
                alt={item.name}
              />
              <div className="flex min-w-0 flex-1 flex-col gap-0.5">
                <p className="truncate text-left font-medium text-text-h">
                  {item.name}
                </p>
                <p className="truncate font-thin text-text">
                  {item.lastMessage}
                </p>
              </div>
              <p className="font-thin text-sm">
                {extractWeekday(item.lastMessageTime ?? "")}
              </p>
            </div>
          ))}
        </>
      )}
    </div>
  );
};

export default SidebarChat;
