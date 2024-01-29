from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()


class Movie(BaseModel):
    id: int
    description: str | None = None
    title: str
    genre: str
    status: str

movies = [Movie(id=i, description=f"Этот фильм показывает {i+10} сцен", title=f"Матрица {i+1} часть", genre='Боевик' , status='создан') for i in range(0, 5)]


@app.get("/", response_model=list[Movie])
async def read_movies():
    logger.info('Отработал GET запрос.')
    return [i for i in movies if i.status != 'удален']


@app.get("/{genre}", response_model=list[Movie])
async def read_movie(genre: str):
    logger.info('Отработал GET с параметром.')
    if genre in [i.genre for i in movies]:
        return [i for i in movies if i.genre == genre]
    logger.info('не верный жанр')
    return HTTPException(status_code=404, detail="Item not found")


@app.post("/", response_model=Movie)
async def create_movies(item: Movie):
    if item.id in [i.id for i in movies]:
       return HTTPException(status_code=404, detail="Item not found")
    movies.append(item)
    return item


@app.put("/{id}", response_model=Movie)
async def edit_movie(id: int, movie: Movie):
    if id in [i.id for i in movies]:
        for i in range(len(movies)):
            if movies[i].id == id:
                movies[i] = movie
                return movies[i]
    return HTTPException(status_code=404, detail="Item not found")


@app.delete("/{id}")
async def delete_movie(id: int):
    for i in range(len(movies)):
        if movies[i].id == id:
            movies[i].status = 'удален'
            return HTTPException(status_code=200, detail="ok")
    return HTTPException(status_code=404, detail="Item not found")
