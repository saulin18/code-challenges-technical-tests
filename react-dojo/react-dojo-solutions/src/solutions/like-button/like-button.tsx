import { useState } from "react";

const appStyle = {
  padding: 24,
  fontFamily: "system-ui",
  background: "var(--bg)",
  minHeight: "100vh",
};

const rowStyle = {
  display: "flex",
  gap: 12,
  alignItems: "center",
};

export default function App() {
  const [likes, setLikes] = useState(141);
  const [isLiked, setIsLiked] = useState(false);

  const handleClick = () => {
    if (isLiked) {
      setLikes(likes - 1);
      setIsLiked(false);
      return;
    }
    setLikes(likes + 1);
    setIsLiked(true);
  };

  return (
    <div style={appStyle}>
      <p style={{ marginBottom: 24, color: "#71717a" }}>Like Button</p>
      <div style={rowStyle}>
        <button
          onClick={handleClick}
          style={{
            backgroundColor: isLiked ? "#ef4444" : "#e5e7eb", 
            color: isLiked ? "white" : "black", 
            padding: "8px 16px",
            borderRadius: 8,
            border: "none",
            cursor: "pointer",
            fontSize: 16,
          }}
        >
          ♥ Like
        </button>
        <span style={{ fontSize: 18 }}>{likes}</span>
      </div>
    </div>
  );
}
