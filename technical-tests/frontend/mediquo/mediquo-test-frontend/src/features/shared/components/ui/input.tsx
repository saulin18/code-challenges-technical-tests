import React from "react";

export interface InputProps extends React.HTMLAttributes<HTMLInputElement> {
  onValueChange?: (value: string) => void;
  icon?: React.ReactNode;
  className?: string;

  ref?: React.RefObject<HTMLInputElement>;
}

export const Input: React.FC<InputProps> = ({
  onValueChange,
  icon,
  className: moreClasses,
  ref,
  ...props
}) => {
  return (
    <div className="relative flex w-full items-center">
      {icon && (
        <span className="pointer-events-none absolute left-3 flex text-text">
          {icon}
        </span>
      )}
      <input
        ref={ref}
        type="text"
        placeholder="Search"
        onChange={(e) => onValueChange?.(e.target.value)}
        className={`w-full rounded-md border border-border bg-background p-2
           ${moreClasses} ${icon ? "pl-10" : ""}`}
        {...props}
      />
    </div>
  );
};
