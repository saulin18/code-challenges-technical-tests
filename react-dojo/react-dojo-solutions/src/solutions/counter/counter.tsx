import React from "react";

type CounterProps = {
  value: number;
  onAdd: () => void;
  onDecrease: () => void;
  restartToCero: () => void;
  addThree: () => void;
};

function Counter({
  value,
  onAdd,
  onDecrease,
  restartToCero,
  addThree,
}: CounterProps) {
  return (
    <>
      <div style={{ padding: 24, fontFamily: "system-ui" }}>
        <p style={{ fontSize: 48, margin: 0, textAlign: "center" }}>
          {/* muestra el valor */}
          {value}
        </p>
        <div
          style={{
            display: "flex",
            gap: 8,
            marginTop: 16,
            justifyContent: "center",
          }}
        >
          <button onClick={() => onAdd()}>+</button>
          <button onClick={() => onDecrease()}>−</button>
          <button onClick={() => restartToCero()}>reset</button>
          <button onClick={() => addThree()}>+3</button>
        </div>
      </div>
    </>
  );
}

export default Counter;
