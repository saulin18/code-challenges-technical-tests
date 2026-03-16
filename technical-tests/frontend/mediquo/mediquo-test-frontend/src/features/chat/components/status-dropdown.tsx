import React, { useCallback, useState } from "react";
import { CheckIcon } from "@/features/shared/components/ui/check-icon";
import { ChevronDownIcon } from "@/features/shared/components/ui/chevron-down-icon";
import { useHandleClickOutside } from "@/features/chat/hooks/useHandleClickOutside";

interface StatusDropdownProps {
  options: { id: string; label: string }[];
  selectedOption: string;
  onSelectOption: (option: string) => void;
  className?: string;
}

export const StatusDropdown: React.FC<StatusDropdownProps> = ({
  options,
  selectedOption,
  onSelectOption,
  className = "",
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClickOutside = useCallback(() => {
    setIsOpen(false);
  }, []);

  const selectedLabel =
    options.find((o) => o.id === selectedOption)?.label ?? selectedOption;

  const containerRef = useHandleClickOutside<HTMLDivElement>(handleClickOutside);

  return (
    <div
      ref={containerRef}
      className={`relative w-full min-w-[140px] ${className}`}
    >
      <button
        type="button"
        onClick={() => setIsOpen((o) => !o)}
        className="flex w-full items-center justify-between gap-2 rounded-md border 
        border-border bg-background px-4 py-2 text-left text-text-h focus:outline-none 
        focus:ring-2 focus:ring-accent focus:ring-offset-0"
      >
        <span className="truncate">{selectedLabel}</span>
        <ChevronDownIcon
          className={`size-5 shrink-0 text-text 
            transition-transform ${isOpen ? "rotate-180" : ""}`}
        />
      </button>

      {isOpen && (
        <ul
          className="absolute top-full left-0 z-50 mt-1 w-full min-w-[120px] rounded-md
           border border-border bg-background py-1 shadow-lg"
          role="listbox"
        >
          {options.map((option) => (
            <li
              key={option.id}
              role="option"
              aria-selected={selectedOption === option.id}
            >
              <button
                type="button"
                onClick={() => {
                  onSelectOption(option.id);
                  setIsOpen(false);
                }}
                className={`flex w-full items-center justify-between gap-2 px-4 py-2 
                  text-left text-sm transition-colors hover:bg-hover 
                  ${selectedOption === option.id ? "bg-hover/50 text-text-h" : "text-text"}`}
              >
                <span>{option.label}</span>
                {selectedOption === option.id && (
                  <CheckIcon className="size-4 shrink-0 text-accent" />
                )}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
