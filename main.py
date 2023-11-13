import json
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Response
import uvicorn
from routers.home_router import router as home_router
from routers.calculate_router import router as calculate_router
from routers.weather_router import router as weather_router
from services import weather_api_service

app = FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_api_keys():
    file = Path("settings.json").absolute()
    if not file.exists():
        print(
            f"WARNING:{file } is not found ,You can not continue, Please see settings.json"
        )
        raise Exception("Settings.json file not found")
    else:
        with open(file) as f:
            settings = json.load(f)
            weather_api_service.api_key = settings.get("api_key")


def configure_routing():
    app.include_router(home_router)
    app.include_router(weather_router)
    app.include_router(calculate_router)


if __name__ == "__main__":
    configure()
    uvicorn.run(app, port=8000, host="localhost")
else:
    configure()
