import React from "react";

function format(ms: number) {
  const total = Math.floor(ms / 10);
  const cs = String(total % 100).padStart(2, "0");
  const s = String(Math.floor(total / 100) % 60).padStart(2, "0");
  const m = String(Math.floor(total / 6000)).padStart(2, "0");
  return `${m}:${s}.${cs}`;
}

type IntervalProps = {
  elapsed: number;
  setElapsed: (elapsed: number) => void;
  running: boolean;
  handleReset: () => void;
  setRunning: (running: boolean) => void;
};
const Interval: React.FC<IntervalProps> = ({
  elapsed,
  running,
  handleReset,
  setRunning
}) => {
  return (
    <div style={{ padding: 24, fontFamily: "system-ui", textAlign: "center" }}>
      <p
        style={{
          fontSize: 48,
          margin: 0,
          fontFamily: "ui-monospace, monospace",
        }}
      >
        {format(elapsed)}
      </p>
      <div
        style={{
          display: "flex",
          gap: 8,
          marginTop: 16,
          justifyContent: "center",
        }}
      >
        <button onClick={() => setRunning(!running)}>
          {running ? "pause" : "start"}
        </button>
        <button
          onClick={() => {
            handleReset();
          }}
        >
          reset
        </button>
      </div>
    </div>
  );
};

export default Interval;
