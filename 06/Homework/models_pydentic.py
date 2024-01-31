from pydantic import BaseModel, Field
import datetime


class User_create(BaseModel):
    name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    date: datetime.date
    email: str = Field(max_length=128, pattern='[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]')
    adres: str = Field(max_length=10)


class User_get(User_create):
    id: int
    status: str