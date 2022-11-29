import os
import time
from http.client import HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from models import models, schemas
from database.database import engine, get_db, SessionLocal

from starlette.requests import Request
from starlette.responses import Response

models.Base.metadata.create_all(bind=engine)

# Date => file1 > file2 => file1 newer than file2

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/node",
    tags=["graph"],
    responses={404: {"description": "Not found"}},
)

def list_file(path):
  return os.listdir(path)
def get_file_modify_date(path_file):
  ti_c = os.path.getctime(path_file)
  ti_m = os.path.getmtime(path_file)
  # Converting the time in seconds to a timestamp
  c_ti = time.ctime(ti_c)
  m_ti = time.ctime(ti_m)
  print(f"The file located at the path {path_file} was created at {c_ti} and was " f"last modified at {m_ti}")
  return c_ti
def compareFileUpdate(previousPath, currentPath):
  previousFile = get_file_modify_date(previousPath)
  currentFile = get_file_modify_date(currentPath)
  if (previousFile > currentFile):
    return previousPath
  elif (previousFile < currentFile):
    return currentPath
  return
def compareFileUpdateList(lists, path):
  newest = ''
  if (len(lists) == 1):
    return path+'/'+lists[0]
  elif (len(lists) > 1):
    for i in range(len(lists)):
      current = path+'/'+lists[i]
      if (i == 0):
        newest = current
        continue
      newest = compareFileUpdate(newest, current)
  return newest

# list_all images, pcap, dot file
@router.get('/getAll')
def getAll(db: Session = Depends(get_db)):
  nodes = db.query(models.Node).all()
  nodes_detail = []
  for node in nodes:
    node_detail = {
      "owner": node.owner,
      "name": node.name,
      "idnode": node.idnode,
      "detail": node.detail,
      'pcaps': list_file('assets/pcaps/'+node.name),
      'images': list_file('assets/images/'+node.name),
      'dots': list_file('assets/dots/'+node.name),
    }
    nodes_detail.append(node_detail)
  return nodes_detail

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

# fetch to got lastest images in each nodes
@router.get('/images/lastest')
def getImageLastInEachNode():
  with SessionLocal() as db:
    nodes = db.query(models.Node)
    lastestImages = []
    for node in nodes:
      print(node.idnode)
      # For Image Path
      files = list_file('assets/images/'+node.name)
      path = 'assets/images/'+node.name
      lastestImage = compareFileUpdateList(files, path)
      lastestImages.append({
        "owner": node.owner,
        "name": node.name,
        "idnode": node.idnode,
        "detail": node.detail,
        'image': lastestImage
      })
  return lastestImages