from fastapi import APIRouter , HTTPException , status ,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from db.data import getDB
from db import models
from db.hash import verify_password
from auth.oauth2 import create_access_token

router = APIRouter(
  tags = ["authentication"]
)

@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(getDB)):
  user = db.query(models.DBUser).filter(models.DBUser.username == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect username or password")
  if not verify_password(request.password, user.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Password is not correct")


  access_token =  create_access_token(
      data={"sub": user.username}
    )

  return {
    "access_token": access_token, 
    "token_type": "bearer",
    "user_id": user.id,
    "user_name": user.username,
    "user": user
  }