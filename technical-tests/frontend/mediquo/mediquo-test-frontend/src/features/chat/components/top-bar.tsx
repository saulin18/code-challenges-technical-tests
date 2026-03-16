import React, { useState } from "react";
import type { User } from "@/features/chat/domain/types";
import { StatusDropdown } from "./status-dropdown";
export interface TopBarProps {
  user: User;
  numberOfMessages?: number;
}

export const TopBar: React.FC<TopBarProps> = ({ user, numberOfMessages }) => {
  const [selectedOption, setSelectedOption] = useState("not_reviewed");

  const options = [
    { id: "good", label: "Good" },
    { id: "bad", label: "Bad" },
    { id: "not_reviewed", label: "Not Reviewed" },
  ];

  const onSelectOption = (option: string) => {
    setSelectedOption(option);
  };
  return (
    <header
      className="flex h-20 shrink-0 flex-col justify-center border-b border-border 
    bg-background px-4 py-2"
    >
      <div className="flex items-center justify-between gap-4">
        <div className="flex items-center gap-2">
          <img
            className="w-10 h-10 shrink-0 object-cover"
            src={user.avatar}
            alt={user.name}
          />
          <p className="font-medium text-text-h">{user.name}</p>
        </div>
        <div className="flex items-center gap-2">
          <StatusDropdown
            options={options}
            selectedOption={selectedOption}
            onSelectOption={onSelectOption}
          />
        </div>
      </div>

      {numberOfMessages && (
        <p className="pl-10 text-left">{numberOfMessages} messages</p>
      )}
    </header>
  );
};
