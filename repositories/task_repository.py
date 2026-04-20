from models.task import Task


class TaskRepository:
    def __init__(self):
        self._tasks: list[Task] = []

    def get_tasks(self) -> list[Task]:
        return self._tasks.copy()
    
    def add_task(self, title: str) -> None:
        self._tasks.append(Task(id=len(self._tasks) + 1, title=title, is_completed=False))


    def get_task(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} not found")

    def mark_task_completed(self, task_id: int) -> None:
        for task in self._tasks:
            if task.id == task_id:
                task.is_completed = True
                break