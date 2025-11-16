from fastapi import FastAPI
from routes.items import router as items_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

app.include_router(items_router)