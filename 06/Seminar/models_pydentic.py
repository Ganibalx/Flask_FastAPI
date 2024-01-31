from pydantic import BaseModel, Field


class User_create(BaseModel):
    username: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(max_length=10)


class User_get(User_create):
    id: int
