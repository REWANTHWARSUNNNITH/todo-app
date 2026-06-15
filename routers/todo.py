from __future__ import annotations
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from typing import List
from models import Todo
from database import get_db
from schemas import TodoResponse, TodoCreate,TodoUpdate
from sqlalchemy.orm import Session

router = APIRouter(prefix="/todos",tags=["Todos"])

# Create A todo
@router.post("/",response_model=TodoResponse)
def create_todo(todo:TodoCreate,db : Session = Depends(get_db)):
    new_todo = Todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
# GET ALL TODO
@router.get("/", response_model=list[TodoResponse])
def get_todos(db:Session = Depends(get_db)):
    return db.query(Todo).all()
# GET BY ID
@router.get("/{todo_id}",response_model=TodoResponse)
def get_todo(todo_id : int , db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404)
    return todo
# UPDATE BY ID
@router.put("/{todo_id}",response_model=TodoResponse)
def update_todo(todo_id:int,updated : TodoUpdate , db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404)
    for key, value in updated.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo
# DELETE BY ID
@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id : int, db:Session = Depends(get_db)):
    todo= db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404)
    db.delete(todo)
    db.commit()
    return