from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import todo
from database import engine,Base

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
app.include_router(todo.router)
@app.get("/")
def root():
    return {"message": "Task flow API is running be carefully done"}