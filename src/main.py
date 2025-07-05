from fastapi import FastAPI
from routes.main_routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Hello from root!"}
