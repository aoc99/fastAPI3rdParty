from distutils.log import error
import time
from typing import Callable
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute

from fastapi import FastAPI
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

apm = make_apm_client({'SERVICE_NAME': 'middleware' , 'SERVER_URL': 'http://10.6.226.246:8200'})
app = FastAPI()
app.add_middleware(ElasticAPM, client=apm)


class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            requests = request
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            print(f"route duration: {duration}")
            print(f"route response headers: {response.headers}")
            try:
                apm.capture_message(jsonable_encoder(requests._body))
                apm.capture_message(jsonable_encoder(response.body))
                return response
            except ZeroDivisionError:
                apm.capture_exception()

                

        return custom_route_handler
