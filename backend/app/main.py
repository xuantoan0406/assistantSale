from fastapi import FastAPI
from app.api.endpoints import user, item

app = FastAPI()


# app.include_router(user.router, prefix="/users", tags=["users"])
# app.include_router(item.router, prefix="/items", tags=["items"])

@app.get("/")
def read_root():
    return {"result": "Hello World"}
