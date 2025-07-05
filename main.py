from fastapi import FastAPI
from src.routes import hello

app = FastAPI()

app.include_router(hello.router)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render!"}
