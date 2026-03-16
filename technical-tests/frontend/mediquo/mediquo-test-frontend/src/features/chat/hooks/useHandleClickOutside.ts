import { useEffect, useRef } from "react";

/**
 * Hook to handle clicks outside a container
 * @param callback - The callback to call when the user clicks outside the container
 * @returns The ref to the container
 */
export const useHandleClickOutside = <T extends HTMLElement>(callback: () => void) => {
  const containerRef = useRef<T>(null);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (
        containerRef.current &&
        !containerRef.current.contains(e.target as Node)
      ) {
        callback();
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [callback]);

  return containerRef;
};
