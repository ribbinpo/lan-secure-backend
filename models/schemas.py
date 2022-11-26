from typing import Optional
from pydantic import BaseModel

# Node
class NodeBase(BaseModel):
  name: str
  owner: str

class NodeCreate(NodeBase):
  detail: str

class Node(NodeBase):
  idnode: int
  detail: str

class NodeUpdate(BaseModel):
  name: Optional[str] = ''
  owner: Optional[str] = ''
  detail: Optional[str] = ''

class NodeId(BaseModel):
  idnode: int

# Admin

class AdminBase(BaseModel):
  email: str
  password: str

class Admin(AdminBase):
  iduser: int