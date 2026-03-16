import React from "react";
import type { Message } from "@/features/chat/domain/types";
import { formatDate } from "@/features/shared/utils/dates";

interface ChatProps {
  messages: Message[];
}

export const ChatContainer: React.FC<ChatProps> = ({ messages }) => {
  if (messages.length === 0) {
    return <span className="flex flex-col gap-4 p-4">No messages found</span>;
  }

  //Profetional messages on the right, patient messages on the left
  return (
    <span className="flex flex-col gap-4 p-4">
      {messages.map((message) => {
        const isProfessional =
          message.sender_id === message.professional.user_id;
        return (
          <div
            key={message.message_id}
            className={`flex ${
              isProfessional ? "justify-end" : "justify-start"
            }`}
          >
            <div className={` px-4 rounded-md p-1 max-w-fit ${
              isProfessional ? "bg-professional" : "bg-patient"
            }`}>
              <p className="text-xs text-bg-patient text-left">
                {formatDate(message.sent_at)}
              </p>
              <p className="text-sm text-left text-mauve-800 ">{message.message}</p>
            </div>
          </div>
        );
      })}
    </span>
  );
};
