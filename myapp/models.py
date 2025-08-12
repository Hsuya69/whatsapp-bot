from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.future import select
from sqlalchemy.orm import declarative_base,relationship
base = declarative_base()

class Person(base):
    __tablename__="people"
    id = Column(Integer,primary_key=True)
    name = Column(String(20),nullable=True)
    age = Column(Integer,nullable=True)
    ph_no=Column(String(30),unique=True)
    step=Column(String(30))

    msgs=relationship("Message",back_populates="peoples")

class Message(base):
    __tablename__="messages"
    msgid = Column(Integer,primary_key=True,autoincrement=False)
    msg= Column(String(369))
    id=Column(Integer,ForeignKey("people.id"))

    peoples=relationship("Person",back_populates="msgs")






