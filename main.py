from fastapi import FastAPI
from src_routes_main_routes import router

app = FastAPI()

app.include_router(hello.router)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render!"}
