import { useMemo } from "react";
import { useParams } from "react-router-dom";
import { ChatContainer } from "@/features/chat/components/chat-container";
import { TopBar } from "@/features/chat/components/top-bar";
import { useRooms } from "@/features/chat/hooks/useRooms";

export function ChatPage() {
  const { roomId } = useParams<{ roomId: string }>();
  const { rooms } = useRooms();

  const room = useMemo(
    () => rooms.find((r) => r.room_id === roomId),
    [rooms, roomId],
  );
  const messages = useMemo(
    () => (Array.isArray(room?.messages) ? room.messages : []),
    [room?.messages],
  );
  const user = room?.user;
  const numberOfMessages = room?.messages?.length;

  return (
    <>
      {user && (
        <TopBar user={user} numberOfMessages={numberOfMessages} />
      )}
      <main className="min-h-0 flex-1 overflow-auto">
        <ChatContainer messages={Array.isArray(messages) ? messages : []} />
      </main>
    </>
  );
}
