from fastapi import APIRouter , Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

# @router.post('/new')
# def createBlog():
#   return {"message": "Blog created successfully"}


class Image(BaseModel):
  url: str
  alias: str

class BlogModel(BaseModel):
  title: str
  body: str
  published: Optional[bool]
  tags: List[str] = []
  matadata: Dict[str, str] = {'key1' :'val1'}
  image:Optional[Image] = None

# @router.post('/new')
# def createBlog(blog: BlogModel):
#   return {"data": blog}


@router.post('/new/{id}')
def createBlog(blog: BlogModel, id: int, version: int = 1):
  return {
    "id": id,
    "data": blog,
    "version": version
  }

@router.post('/all/{id}/comment')
def commentOnBlog(blog: BlogModel, id: int, commentTitle = Query(None ,
       alias="comment_title", # For chagne the name of the query parameter
       title="The title of the comment", 
       description="The title of the comment",
      ),
      content: str = Body(...,
       min_length=10,
       max_length=15,
       example="This is a comment",
       regex="^[a-z\s]*$"
      ),
      v:Optional[List[str]] = Query(['1.0', '1.1', '1.2']),
      commentId:int = Path(..., gt=5,lt=10),
    ):
  return {
    "data": blog,
    "id": id,
    "content": content,
    "version": v,
    "commentId": commentId,
    "commentTitle": commentTitle,
    }


def requiredFunctionality():
  return {"message": "Learning  FastAPI is Important"}