import requests

from src.Services.ToDoService import ToDo, ToDoService
from src.Services.StorageService import StorageService

TODO_API_URL = "https://jsonplaceholder.typicode.com/todos/"


class ApiService:
    def __init__(self):
        self.to_do_service = ToDoService()
        self.storage_service = StorageService()

    def run(self):
        todos: list[ToDo] = self.fetch_todos()
        todos = self.to_do_service.set_todos(todos)
        self.storage_service.save_todos(todos)
        return todos

    def fetch_todos(self) -> list[ToDo]:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        response.raise_for_status()
        return response.json()