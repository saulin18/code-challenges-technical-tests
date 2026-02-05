from typing import TypedDict


class ToDo(TypedDict):
    id: int
    userId: int
    title: str
    completed: bool


class ToDoService:
    def __init__(self):
        self.todos = []

    def set_todos(self, todos: list[ToDo]) -> list[ToDo]:
        self.todos = todos
        return self.todos
