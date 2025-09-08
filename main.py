from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from loguru import logger
from routes.recipes import router


logger.remove()
logger.add("logs.log", level="INFO", format="{time} {level} {message}", rotation="10 MB")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)