import { useReducer } from "react";

type todoItem = {
  id: number;
  text: string;
  done: boolean;
};

type todosState = {
  items: todoItem[];
  next: number;
};

const initial: todosState = { items: [], next: 1 };

type todoAction =
  | { type: "add"; text: string }
  | { type: "toggle"; id: number }
  | { type: "remove"; id: number };

type TodoActionType = todoAction["type"];

const mapTypeToAction: {
  [K in TodoActionType]: (
    state: todosState,
    action: Extract<todoAction, { type: K }>,
  ) => todosState;
} = {
  add: (state, action) => {
    const newItem: todoItem = {
      id: state.next,
      text: action.text,
      done: false,
    };
    return { ...state, items: [...state.items, newItem], next: state.next + 1 };
  },
  toggle: (state, action) => {
    return {
      ...state,
      items: state.items.map((item) =>
        item.id === action.id ? { ...item, done: !item.done } : item,
      ),
    };
  },
  remove: (state, action) => {
    return {
      ...state,
      items: state.items.filter((item) => item.id !== action.id),
    };
  },
};

function reducer(state: todosState, action: Extract<todoAction, { type: TodoActionType }>): todosState {
   switch (action.type) {
    case "add":
      return mapTypeToAction.add(state, action)
      
    case "toggle":
      return mapTypeToAction.toggle(state, action)

    case "remove":
      return mapTypeToAction.remove(state, action) 
    default:
      return state;
   }
}
export default function TodoList() {
  const [state, dispatch] = useReducer(reducer, initial);

  return (
    <div style={{ padding: 24, fontFamily: "system-ui" }}>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          const text = e.currentTarget.text.value.trim();
          if (text) dispatch({ type: "add", text });
          e.currentTarget.reset();
        }}
      >
        <input
          name="text"
          placeholder="agregar tarea..."
          autoFocus
          style={{ width: "100%" }}
        />
      </form>
      <ul style={{ paddingLeft: 18, marginTop: 12 }}>
        {state.items.map((it) => (
          <li
            key={it.id}
            style={{
              textDecoration: it.done ? "line-through" : "none",
              marginBottom: 4,
            }}
          >
            <span
              onClick={() => dispatch({ type: "toggle", id: it.id })}
              style={{ cursor: "pointer" }}
            >
              {it.text}
            </span>
            <button
              onClick={() => dispatch({ type: "remove", id: it.id })}
              style={{ marginLeft: 8 }}
            >
              ×
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
