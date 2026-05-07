import "./App.css";
import { useCounter } from "./solutions/counter/useCounter";
import Counter from "./solutions/counter/counter";
import Input from "./solutions/auto-focus/input";
import { useInputAndFocus } from "./solutions/auto-focus/useInputAndFocus";
import { useInterval } from "./solutions/intervals/useInterval";
import Interval from "./solutions/intervals/interval";
import { FilteredList } from "./solutions/filtered-list/filtered-list";
import { UseMemoFilter } from "./solutions/use-memo-filter/UseMemoFilter";
import { OptimisticLikes } from "./solutions/optimistic-like/OptimisticLike";
import TodoList from "./solutions/intermediate/todo-list-with-reducer/ToDoList";
import FetchUsers from "./solutions/intermediate/fetch-user-abort-controller/FetchUsers";
import LazyImport from "./solutions/advanced/lazy-import/Lazy";
import DefferedSearch from "./solutions/advanced/deffered-value/DefferedSearch";
import FormReducer from "./solutions/intermediate/form-reducer/FormReducer";
import FormActionState from "./solutions/intermediate/use-action-state/FormActionState";
import TransitionTabs from "./solutions/intermediate/transition-tabs/TransitionTabs";
function App() {
  const { value, addOne, decreaseOne, restartToCero, addThree } = useCounter();
  const { text, setText, doManualFocus, inputRef, renderCounter } =
    useInputAndFocus();
  const { elapsed, setElapsed, handleReset, running, setRunning } =
    useInterval();

  return (
    <>
      <section id="center">
        <Counter
          value={value}
          onAdd={addOne}
          onDecrease={decreaseOne}
          restartToCero={restartToCero}
          addThree={addThree}
        />

        <Input
          text={text}
          setText={setText}
          doManualFocus={doManualFocus}
          ref={inputRef}
          renderCounter={renderCounter}
        />

        <Interval
          elapsed={elapsed}
          setElapsed={setElapsed}
          handleReset={handleReset}
          running={running}
          setRunning={setRunning}
        />

        <FilteredList />

        <UseMemoFilter />

        <OptimisticLikes />
      </section>

      <section>
        <h2>Intermediate</h2>

        <TodoList />

        <FetchUsers />

        <FormReducer />

        <FormActionState />

        <TransitionTabs />
      </section>

      <section>
        <h2>Advanced</h2>
        <LazyImport />
        <DefferedSearch />
      </section>

      <div className="ticks"></div>
      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  );
}

export default App;
