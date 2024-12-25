from fastapi import FastAPI, requests
from flask import Flask, render_template
from fastapi.middleware.wsgi import WSGIMiddleware
from routes.todo import todo

app = FastAPI()
flask_app = Flask(__name__)
app.mount("/home", WSGIMiddleware(flask_app))
app.include_router(todo)


@flask_app.get("/")
def index_page():
    return render_template("index.html")


@app.get("/")
def root():
    pass
