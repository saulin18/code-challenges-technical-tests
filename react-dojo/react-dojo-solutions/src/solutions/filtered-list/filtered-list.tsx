import React from "react";

import { useState } from "react";

const FRUTAS = [
  "Manzana",
  "Banana",
  "Cereza",
  "Durazno",
  "Uva",
  "Kiwi",
  "Limón",
  "Mango",
  "Naranja",
  "Pera",
  "Piña",
  "Sandía",
  "Fresa",
  "Melón",
  "Ciruela",
];

export function FilteredList() {
  const [query, setQuery] = useState("");

  const filteredFruits = FRUTAS.filter((fruta) => fruta.toLowerCase().includes(query.toLowerCase()));

  const isEmpty = filteredFruits.length === 0;

  return (
    <div style={{ padding: 24, fontFamily: "system-ui", maxWidth: 320 }}>
      <div style={{ display: "flex", gap: 8, marginBottom: 12 }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Buscar fruta..."
          style={{ flex: 1 }}
        />
        <button onClick={() => setQuery("")}>limpiar</button>
      </div>

      {isEmpty ? (
        <div>Sin resultados</div>
      ) : (
        <ul style={{ listStyle: "none", padding: 0, marginTop: 8 }}>
          <div>
            {filteredFruits.map((fruta) => {
              return <div key={fruta.toLowerCase()}>{fruta}</div>;
            })}
          </div>
        </ul>
      )}
    </div>
  );
}
