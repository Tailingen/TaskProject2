from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

db_immitation = [
    {"id": 1, "text": "Подоить корову", "status": False},
    {"id": 2, "text": "Погулять с собакой", "status": False}
]

class TaskAddSchema(BaseModel):
    text: str = Field(min_length=2, max_length=255)
    status: bool

@app.get("/home/")
async def home():
    return "Home"

@app.get("/about/")
async def about():
    return "Страница о сайте"

@app.get("/tasks/{task_id}/")
async def task(task_id: int):
    if 0 < int(task_id) <= len(db_immitation):
        return db_immitation[task_id-1]["text"]
    else:
        return "Запись не найдена"

@app.get("/tasks/")
async def tasks():
    return db_immitation

@app.post("/tasks/create/")
async def task_create(schema: TaskAddSchema):
    db_immitation.append({"id": len(db_immitation)+1, "text": schema.text, "status": schema.status})
    return db_immitation[-1]

@app.put("/tasks/{task_id}/update/")
async def task_update(task_id: int, schema: TaskAddSchema):
    db_immitation[task_id-1] = {"id": task_id, "text": schema.text, "status": schema.status}
    return db_immitation[task_id-1]

@app.delete("/tasks/{task_id}/delete/")
async def task_delete(task_id: int):
    res = db_immitation.pop(task_id-1)
    return res