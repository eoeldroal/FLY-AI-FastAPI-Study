from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from typing import List

from database.orm import ToDo

def get_todos(session : Session) -> List[ToDo] :
    return list(session.execute(select(ToDo)))

def get_todo_by_todo_id(session : Session, todo_id : int) -> ToDo  | None:
    return session.scalar(select(ToDo).where(ToDo.id == todo_id))

def create_todo(session : Session, todo : ToDo) :
    session.add(instance = todo)
    session.commit()
    session.refresh(instance = todo)
    return todo

def update_todo(session : Session, todo : ToDo) :
    session.add(instance = todo)
    session.commit()
    session.refresh(instance = todo)
    return todo

def delete_todo(session : Session, todo_id : int) -> None :
    session.execute(delete(ToDo).where(ToDo.id == todo_id))
    session.commit()