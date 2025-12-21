from fastapi import FastAPI
from app.database.db import engine
from app.database import models
from app.routers import auth

models.Base.metadata.create_all(bind=engine)


app= FastAPI(title="Task Manager API")

app.include_router(auth.router)

@app.get("/")
def health_check():
    return {"status" : "Task Manager API is running"}


