from fastapi import FastAPI
from ser_routes_main_routes imort router

app = FastAPI()

app.include_router(hello.router)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render!"}
