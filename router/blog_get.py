from fastapi import APIRouter,status, Response, Depends
from enum import Enum
from typing import Optional
from router.blog_post import requiredFunctionality

router = APIRouter(
  prefix='/blog',
  tags=['blog']
)



# @router.get('/all')
# def getAllBlogs():
#   return { "message" : "All blogs Provded"}


@router.get(
  '/all',
  summary="Get all blogs",
  description="This api call simulates fetching all blogs",
  response_description="The list of avilable blog ",
  )
def getAllBlogs(page  = 1, offset: Optional[int] = None, req_paramter:dict = Depends(requiredFunctionality)):
  return { "message" : f"All {offset} blogs Provded on page {page}" , "req ": req_paramter}

@router.get('/{id}/comments/{comment_id}', tags=[ 'comments'] )
def getComment(id: int, comment_id: int, valid:bool= True, username:Optional[str] = None):
  """
  Simulates retrivieing a commne t of a blog 

  - **id**: int - The id of the blog
  - **comment_id**: int - The id of the comment
  - **valid**: bool - The validity of the comment
  - **username**: str - The username of the user who made the comment 


  """
  return {"message" : f"Comment with id {comment_id} for blog {id}", "valid": valid, "username": username}

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'


@router.get('/type/{type}', )
def getBlogType(type: BlogType):
  return { "message" : f"Blog with type {type}"}


@router.get('/{id}', status_code=status.HTTP_200_OK,  )
def getBody(id: int, response: Response):
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {"error" : "Blog not found"}
  else:
    response.status_code = status.HTTP_200_OK
    return { "message" : f"Blog with id {id}"}
