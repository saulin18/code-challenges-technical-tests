import { useReducer } from "react";

type State = {
  values: { email: string; password: string; confirm: string };
  touched: { email: boolean; password: boolean; confirm: boolean };
  submitted: boolean;
};

const initialState: State = {
  values: { email: "", password: "", confirm: "" },
  touched: { email: false, password: false, confirm: false },
  submitted: false,
};

function validate(values: {
  email: string;
  password: string;
  confirm: string;
}) {
  const errors: { email?: string; password?: string; confirm?: string } = {};
  if (!/^\S+@\S+\.\S+$/.test(values.email)) errors.email = "email inválido";
  if (values.password.length < 6) errors.password = "mínimo 6 caracteres";
  if (values.confirm !== values.password) errors.confirm = "no coincide";
  return errors;
}

function reducer(
  state: State,
  action: { type: string; field: string; value: string },
) {
  switch (action.type) {
    case "change":
      // TODO: actualiza values[action.field]
      return {
        ...state,
        values: { ...state.values, [action.field]: action.value },
      };
    case "blur":
      // TODO: marca touched[action.field] = true
      return { ...state, touched: { ...state.touched, [action.field]: true } };
    case "submit":
      // TODO: marca submitted = true
      return { ...state, submitted: true };
    default:
      return state;
  }
}

export default function FormReducer() {
  const [state, dispatch] = useReducer(reducer, initialState);
  const errors = validate(state.values);
  const hasErrors = Object.keys(errors).length > 0;

  function field(name: string, type = "text") {
    const showError = (state.touched[name] || state.submitted) && errors[name];
    return (
      <div style={{ marginBottom: 12 }}>
        <input
          type={type}
          placeholder={name}
          value={state.values[name]}
          onChange={(e) =>
            dispatch({ type: "change", field: name, value: e.target.value })
          }
          onBlur={() => dispatch({ type: "blur", field: name, value: "" })}
          style={{ width: "100%" }}
        />
        {showError && (
          <small style={{ color: "var(--error, #c98b82)" }}>
            {errors[name]}
          </small>
        )}
      </div>
    );
  }

  if (state.submitted && !hasErrors) {
    return <p style={{ padding: 24, fontFamily: "system-ui" }}>enviado ✓</p>;
  }

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        dispatch({ type: "submit", field: "submit", value: "" });
      }}
      style={{ padding: 24, fontFamily: "system-ui", maxWidth: 360 }}
    >
      {field("email", "email")}
      {field("password", "password")}
      {field("confirm", "password")}
      <button type="submit" disabled={hasErrors}>
        crear cuenta
      </button>
    </form>
  );
}
