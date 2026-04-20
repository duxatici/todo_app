import logging

from repositories.task_repository import TaskRepository
from models.task import Task

logger = logging.getLogger(__name__)

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, title: str) -> None:
        logger.info(f"Adding task: {title}")
        self.repository.add_task(title)

    def get_tasks(self) -> list[Task]:
        logger.info("Getting tasks")
        return self.repository.get_tasks()
    

    def get_task(self, task_id: int) -> Task:
        logger.info(f"Getting task {task_id}")
        return self.repository.get_task(task_id)
    

    def mark_task_completed(self, task_id: int) -> None:
        logger.info(f"Marking task {task_id} as completed")
        self.repository.mark_task_completed(task_id)