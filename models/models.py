from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base

class Node(Base):
    __tablename__ = "node"

    idnode = Column(Integer, primary_key=True, index=True)
    name = Column(String(10), unique=True, index=True)
    detail = Column(String(200))
    owner = Column(String(45))

class User(Base):
    __tablename__ = "user"
    
    iduser = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(45))