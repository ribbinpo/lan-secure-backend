from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from models import models, schemas
from database.database import engine, SessionLocal, get_db

models.Base.metadata.create_all(bind=engine)

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/auth",
    tags=["graph"],
    responses={404: {"description": "Not found"}},
)

@router.post('/signin')
def signin(db: Session = Depends(get_db), user: schemas.AdminBase = {}):
  admin = db.query(models.User).filter(models.User.email == user.email, models.User.password == user.password).first()
  if (admin):
    return {
      "status": "success",
      "detail": admin
    }
  return { "status": "failed" }