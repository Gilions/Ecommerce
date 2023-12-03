from fastapi import FastAPI
from settings.conf import settings

app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "World"}
