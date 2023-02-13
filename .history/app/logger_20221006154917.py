import time
from typing import Callable
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute


class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            requests = request
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            print(f"route request: {request}")
            print(f"route duration: {duration}")
            print(f"route response: {jsonable_encoder(response)}")
            print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler
