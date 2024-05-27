from fastapi import FastAPI
from core.config import Settings

settings = Settings()
app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/")
def hello():
    return {"msg":"Hello FastAPI 🚀"}

@app.get("/hello")
def hello1():
    return {"msg":"Hello FastAPIIIIII 🚀"}