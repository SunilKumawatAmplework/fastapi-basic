from pydantic import BaseModel
from typing import List


#  Article user Display
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config():
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    id: int
    username: str
    email: str
    items: List[Article] = []

    # password: str
    class Config():
        orm_mode = True


# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    id:int
    title: str
    content: str
    published: bool
    user: User

    class Config():
        orm_mode = True
