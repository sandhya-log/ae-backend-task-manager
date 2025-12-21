from fastapi import FastAPI
from app.database.db import engine
from app.database import models

models.Base.metadata.create_all(bind=engine)


app= FastAPI(title="Task Manager API")

@app.get("/")
def health_check():
    return {"status" : "Task Manager API is running"}


