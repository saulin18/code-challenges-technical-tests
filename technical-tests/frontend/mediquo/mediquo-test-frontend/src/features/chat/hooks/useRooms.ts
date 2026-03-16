import { useEffect, useState } from "react";
import list from "@/storage/list.json";
import type { Room } from "@/features/chat/domain/types";

/**
 * Hook for getting the rooms from the json file in src/storage/list.json
 */
export const useRooms = () => {
  const [rooms, setRooms] = useState<Room[]>([]);

  useEffect(() => {
    const normalized = list.data.map((room) => ({
      ...room,
      messages: Array.isArray(room.messages)
        ? [...room.messages].reverse()
        : room.messages,
    }));
    setRooms(normalized);
  }, []);

  const sidebarItemsArr = rooms.map((room) => ({
    id: room.room_id,
    name: room.user.name,
    icon: room.user.avatar,
    lastMessage: room.messages?.[room.messages.length - 1]?.message || "",
    lastMessageTime: room.messages?.[room.messages.length - 1]?.sent_at || "",
  }));

  return {
    rooms,
    sidebarItemsArr
  };
};
