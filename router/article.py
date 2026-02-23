from fastapi import APIRouter, Depends, HTTPException
from schemas import ArticleBase, ArticleDisplay 
from sqlalchemy.orm import Session
from db.data import getDB
from db import db_article
from typing import List
from auth.oauth2 import oauth2_scheme, get_current_user
from schemas import UserBase

router = APIRouter(prefix="/article", tags=["article"])

@router.get("/", response_model=List[ArticleDisplay])
def get_all_aarticle(db: Session = Depends(getDB)):
    return db_article.get_all_article(db)

@router.post("/create", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(getDB), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)

@router.get("/{id}",) # response_model=ArticleResponse)
def get_article(id: int, db: Session = Depends(getDB), current_user: UserBase = Depends(get_current_user)):
    article = db_article.get_article(db, id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return {
        "data": article,
        "current_user": current_user
    }
    



