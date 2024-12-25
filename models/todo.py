from pydantic import BaseModel


class Todos(BaseModel):
    Title: str
    Desc: str
