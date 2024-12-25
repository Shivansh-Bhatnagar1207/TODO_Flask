from fastapi import APIRouter, Request
from schema.todo import todoEntity, todosEntity
from config.db import conn

todo = APIRouter()


@todo.get("/")
async def read_items(request: Request):
    docs = conn.flask.todos.find({})
    newdocs = []
    for doc in docs:
        newdocs.append(
            {
                "id": doc["_id"],
                "title": doc["title"],
                "desc": doc["desc"],
            }
        )

        return {
            "request": request,
            "newdocs": newdocs,
        }


@todo.post("/")
async def create_items(request: Request):
    form = await request.form()
    fromdict = dict(form)
    todo = conn.flask.todo.insert_one(fromdict)
    return {"data": "entered Sucessfully"}
