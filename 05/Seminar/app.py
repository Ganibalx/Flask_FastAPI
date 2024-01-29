from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    description: str | None = None
    title: str
    status: str

tasks = [Item(id=i, description=f"Сделать {i} отжиманий", title=f"Это задача {i}", status='выполнить') for i in range(0, 10)]


@app.get("/", response_model=list[Item])
async def read_tasks():
    return tasks


@app.get("/{id}", response_model=Item)
async def read_task(id: int):
    if id in [i.id for i in tasks]:
       return [i for i in tasks if i.id == id][0]
    return HTTPException(status_code=404, detail="Item not found")


@app.post("/", response_model=Item)
async def create_task(item: Item):
    if item.id in [i.id for i in tasks]:
       return HTTPException(status_code=404, detail="Item not found")
    tasks.append(item)
    return item


@app.put("/{id}", response_model=Item)
async def edit_task(id: int, task:Item):
    if id in [i.id for i in tasks]:
        for i in range(len(tasks)):
            if tasks[i].id == id:
                tasks[i] = task
                return tasks[i]
    return HTTPException(status_code=404, detail="Item not found")


@app.delete("/{id}")
async def delete_task(id: int):
    for i in range(len(tasks)):
        if tasks[i].id == id:
            tasks[i].status = 'delete_task'
            return HTTPException(status_code=200, detail="ok")
    return HTTPException(status_code=404, detail="Item not found")
