import React, { useCallback, useEffect } from "react";

export const useInterval = () => {
    const intervalRef = React.useRef<ReturnType<typeof setInterval> | null>(null);
    const [elapsed, setElapsed] = React.useState(0);
    const [running, setRunning] = React.useState(true);

    useEffect(() => {

        if (!running) {
            clearInterval(intervalRef.current!);
            intervalRef.current = null;
            return;
        }

        console.log("setting interval");

        if (!intervalRef.current && running) {
            intervalRef.current = setInterval(() => {
                setElapsed((elapsed) => elapsed + 10);
            }, 10);
        }
        return () => {
            clearInterval(intervalRef.current!);
        };
    }, [running]);

    const handleReset = useCallback(() => {
        setElapsed(0);
        setRunning(false);
        clearInterval(intervalRef.current!);
        intervalRef.current = null;
    }, []);


    return {
        elapsed,
        setElapsed,
        handleReset,
        running,
        setRunning,
    };
};
