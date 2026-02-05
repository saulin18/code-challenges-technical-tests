from datetime import datetime
import csv
from pathlib import Path
from src.Services.ToDoService import ToDo

path_to_storage = Path(__file__).parent.parent.parent / "storage"


class StorageService:
    def __init__(self):
        pass

    def save_todos(self, todos: list[ToDo]) -> None:
        for todo in todos:
            filename = self.get_filename(todo)
            self.save_in_csv(todo, filename)

    def get_filename(self, todo: ToDo) -> str:
        now = datetime.now()
        return f"{now.strftime('%y_%m_%d')}_{todo['id']}.csv"

    def save_in_csv(self, todo: ToDo, filename: str) -> None:
        fieldnames = list(todo.keys())
        with open(path_to_storage / filename, "w") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(todo)
        
