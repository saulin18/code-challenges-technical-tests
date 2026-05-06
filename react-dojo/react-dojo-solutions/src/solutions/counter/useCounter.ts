import { useState } from "react"


export const useCounter = () => {
    const [value, setValue] = useState(0)

    const addOne = () => setValue(value + 1)
    const decreaseOne = () => setValue(value - 1)
    const restartToCero = () => setValue(0)

    const handleAddThree = () => {
        setValue(value => value + 1)
        setValue(value => value + 1)
        setValue(value => value + 1)
    }

    return {
        value,
        addOne,
        decreaseOne,
        restartToCero,
        addThree: handleAddThree
    }
}