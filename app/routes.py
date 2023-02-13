# from fastapi import APIRouter
# from pydantic import BaseModel
# from app.logger import TimedRoute

# class MainMessage(BaseModel):
#     message: str = "Profil Maturitas API"

# router = APIRouter(route_class=TimedRoute,tags=["Main"])

# @router.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}


import importlib
import os
from fastapi.responses import ORJSONResponse
from fastapi_pagination import add_pagination
from starlette.types import ASGIApp
from app.helpers import join_path
from app.responses import HttpMainResponse, HttpInternalServerErrorResponse
from app.schemas import MainResponse, InternalServerErrorResponse


def load_routes(app: ASGIApp) -> None:
    @app.get(
        "/",
        summary="Main",
        tags=["Main"],
        response_model=MainResponse,
        responses={
            200: {"model": MainResponse},
            500: {"model": InternalServerErrorResponse},
        }
    )
    def index() -> ORJSONResponse:
        try:
            return HttpMainResponse()
        except Exception as exc:
            exception = str(exc)
            app.logger.error(exception)
            return HttpInternalServerErrorResponse(exception)

    for curr_dir, _, files in os.walk("./api"):
        if "controller.py" in files:
            api_module = curr_dir.replace("./", "").replace("/", ".")
            module_name = api_module.split(".")[-1]
            route_module = importlib.import_module(
                api_module + ".controller", module_name)
            # print(route_module)
            app.include_router(route_module.router)
