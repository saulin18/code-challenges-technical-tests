import React, { useEffect } from "react";
import { useCallback, useState } from "react";

export const useInputAndFocus = () => {



    const [text, setText] = useState("");
    const inputRef = React.useRef<HTMLInputElement>(null)
    const renderCounter = React.useRef(0)

    const doManualFocus = useCallback(() => {
        inputRef.current?.focus()
    }, []);

    const handleSetText = useCallback((text: string) => {
        setText(text)
    }, [])

    useEffect(() => {
        if (inputRef.current) {
            inputRef.current.focus()
        }
        renderCounter.current += 1;

        return () => {
        }
    }, [])


    return { text, setText: handleSetText, doManualFocus, inputRef, renderCounter: renderCounter.current };
}