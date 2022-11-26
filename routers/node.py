from http.client import HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from models import models, schemas
from database.database import engine, get_db, SessionLocal

from starlette.requests import Request
from starlette.responses import Response

models.Base.metadata.create_all(bind=engine)

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/node",
    tags=["graph"],
    responses={404: {"description": "Not found"}},
)

@router.get('/getAll')
def getAll(db: Session = Depends(get_db)):
  return db.query(models.Node).all()

@router.post('/create')
def create(db: Session = Depends(get_db), node: schemas.NodeCreate = { 'name': '', 'owner': '', 'detail': '' }):
  db_node = models.Node(name=node.name, owner=node.owner, detail=node.detail)
  db.add(db_node)
  db.commit()
  db.refresh(db_node)
  return db_node

@router.patch('/update/{node_id}')
def update(request: Request, node_id: int, payload: schemas.NodeUpdate):
  with SessionLocal() as db:
    db_node = db.query(models.Node).filter(models.Node.idnode == node_id).first()
    if not db_node:
      raise HTTPException(status_code=404, detail="Node not found")
    db_node.name = payload.name
    db_node.detail = payload.detail
    db_node.owner = payload.owner
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node

@router.delete('/{node_id}')
def delete(node_id: int):
  with SessionLocal() as db:
    db_node = db.query(models.Node).filter(models.Node.idnode == node_id).first()
    if not db_node:
      raise HTTPException(status_code=404, detail="Node not found")
    db.delete(db_node)
    db.commit()
    return node_id