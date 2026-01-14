import { useState, useRef, useEffect } from "react";
import type { Task } from "../types";

export const useTaskElapsedTime = (task: Task) => {
  const [elapsedTime, setElapsedTime] = useState<number>(0);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    const calculateElapsed = () => {
      const start = new Date(task.startingTime).getTime();
      const now = Date.now();
      const elapsed = Math.floor((now - start) / 1000);
      setElapsedTime(elapsed);
    };

    calculateElapsed();

    intervalRef.current = setInterval(calculateElapsed, 1000);

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [task.startingTime]);

  const formatElapsedTime = (seconds: number): string => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;

    if (hours > 0) {
      return `${hours}h ${minutes}m ${secs}s`;
    } else if (minutes > 0) {
      return `${minutes}m ${secs}s`;
    } else {
      return `${secs}s`;
    }
  };

  return {
    elapsedTime,
    formatElapsedTime,
  };
};
