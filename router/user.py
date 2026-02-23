from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.data import getDB
from db import db_user
from typing import List
from auth.oauth2 import get_current_user


router = APIRouter(prefix="/user", tags=["users"])


# Create User
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(getDB)):
    return db_user.createUser(db, request)


# Read All User
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(getDB), current_user: UserBase = Depends(get_current_user)):
    return db_user.get_all_users(db)


# Read User By Id
@router.get("/{id}", response_model=UserDisplay)
def get_user_by_id(
    id: int,
    db: Session = Depends(getDB),
    current_user: UserBase = Depends(get_current_user)
):
    return db_user.get_user_by_id(db, id)


# Update User


@router.post(
    "/{id}/update",
)
def get_update_user(
    id: int,
    request: UserBase,
    db: Session = Depends(getDB),
    current_user: UserBase = Depends(get_current_user)
):
    return db_user.update_user(db, id, request)


# Delete User


@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(getDB),current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user_data(db, id)
