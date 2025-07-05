from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/hello")
def say_hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}


app = FastAPI()
app.include_router(router)
