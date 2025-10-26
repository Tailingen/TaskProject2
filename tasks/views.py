from fastapi import APIRouter

from tasks.schemas import TaskAddSchema

router = APIRouter()

db_immitation = [
    {"id": 1, "text": "Подоить корову", "status": False},
    {"id": 2, "text": "Погулять с собакой", "status": False}
]

@router.get("/tasks/{task_id}/")
async def task(task_id: int):
    if 0 < int(task_id) <= len(db_immitation):
        return db_immitation[task_id-1]["text"]
    else:
        return "Запись не найдена"

@router.get("/tasks/")
async def tasks():
    return db_immitation

@router.post("/tasks/create/")
async def task_create(schema: TaskAddSchema):
    db_immitation.append({"id": len(db_immitation)+1, "text": schema.text, "status": schema.status})
    return db_immitation[-1]

@router.put("/tasks/{task_id}/update/")
async def task_update(task_id: int, schema: TaskAddSchema):
    db_immitation[task_id-1] = {"id": task_id, "text": schema.text, "status": schema.status}
    return db_immitation[task_id-1]

@router.delete("/tasks/{task_id}/delete/")
async def task_delete(task_id: int):
    res = db_immitation.pop(task_id-1)
    return res