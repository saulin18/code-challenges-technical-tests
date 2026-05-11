import React, { useState } from "react";

export default function App() {
  const [error, setError] = useState({ name: "", email: "" });
  const [form, setForm] = useState({ name: "", email: "" });
  const [success, setSuccess] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();
    const { name, email } = form;

    const emptyName = !name;
    const invalidEmail = !email.includes("@");
    const hasError = emptyName || invalidEmail;
    if (hasError) {
      setError({
        name: emptyName ? "El nombre no puede estar vacío" : "",
        email: invalidEmail ? "El email debe contener @" : "",
      });
      setSuccess(false);
      return;
    }
    setSuccess(true);
    return
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ padding: 24, fontFamily: "system-ui" }}
    >
      <div style={{ marginBottom: 16 }}>
        <input
          name="name"
          onChange={handleChange}
          placeholder="nombre"
          style={{ padding: 8, fontSize: 16, width: "100%" }}
        />
        {error.name && <p style={{ color: "red", fontSize: 14 }}>{error.name}</p>}
      </div>
      <div style={{ marginBottom: 16 }}>
        <input
          name="email"
          onChange={handleChange}
          placeholder="email"
          style={{ padding: 8, fontSize: 16, width: "100%" }}
        />
        {error.email && <p style={{ color: "red", fontSize: 14 }}>{error.email}</p>}
      </div>
      <button type="submit" style={{ padding: "8px 16px", fontSize: 16 }}>
        Enviar
      </button>
      {success && <p style={{ color: "green", fontSize: 14 }}>Formulario enviado con éxito</p>}
    </form>
  );
}
