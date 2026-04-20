import logging
from fastapi import FastAPI, Query, HTTPException

from services.task_service import TaskService
from repositories.task_repository import TaskRepository
from models.task import Task

logging.basicConfig(
    level=logging.INFO,
    filename="todo_app.log",
    filemode="a",
    format="%(asctime)s - %(name)s - [%(levelname)s] - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI()

repository = TaskRepository()
service = TaskService(repository)


@app.get("/tasks/")
def read_tasks():
    return service.get_tasks()


@app.post("/tasks/")
def create_task(task: Task):
    service.add_task(task.title)


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    return service.get_task(task_id)
    

@app.get("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    service.mark_task_completed(task_id)