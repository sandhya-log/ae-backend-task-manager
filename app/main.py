from fastapi import FastAPI
from app.database.db import engine
from app.database import models
from app.routers import auth, protected


app= FastAPI(title="Task Manager API")

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(protected.router)

@app.get("/")
def health_check():
    return {"status" : "Task Manager API is running"}


