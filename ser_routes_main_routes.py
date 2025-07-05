from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def say_hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}

/hello endpoint in main_routes.py
