import os
from fastapi import FastAPI, Request, status
from router import blog_get
from router import blog_post
from db import models
from db.data import engine
from router import user, article, product, file
from exceptions import StoryException
from fastapi.responses import JSONResponse
from auth import authentication
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/")
def index():
    return {"id": "1", "name": "Hello", "lname": "world"}


# @app.exception_handler(StoryException)
# def story_exception_handler(request: Request, exc: StoryException):
#     return JSONResponse(
#         status_code=status.HTTP_418_IM_A_TEAPOT,
#         content={"message": exc.name},
#     )


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT,
        content={"details": exc.name},
    )


@app.on_event("startup")
def on_startup():
    models.Base.metadata.create_all(engine)


# Ensure the files directory exists for static file serving
os.makedirs("files", exist_ok=True)
app.mount("/files", StaticFiles(directory="files"), name="files")
