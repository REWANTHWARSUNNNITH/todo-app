from typing import Optional

from pydantic import BaseModel

class TodoCreate(BaseModel):
    title:str
    description:Optional[str]
    completed:bool=False
class TodoUpdate(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    completed:Optional[bool]=False
class TodoResponse(BaseModel):
    id : int
    title : str
    description : str|None
    completed : bool

    # class Config:
    #     from_attribute = True
    model_config = {"from_attributes" :True}