from textwrap import indent
import time, json, os
from loguru import logger
from typing import Callable
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute
from starlette.datastructures import Headers
from starlette.background import BackgroundTask

# logger.basicConfig(filename='info.log', level=logging.DEBUG)

def log_info(req_body, res_body, request):
    before = time.time()
    duration = time.time() - before
    logger.info("[REQUEST {} - {}] : {}", request.method, str(request.url), jsonable_encoder(req_body.decode()))
    logger.info("[RESPONSE {} - {}] : {} duration {}", request.method, str(request.url),
                        json.dumps(json.loads(res_body.decode()), indent=4), duration)
       
class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            req_body = await request.body()
            response = await original_route_handler(request)
            res_body = response.body
            response.background = BackgroundTask(log_info, req_body, res_body, request)
            return response

        return custom_route_handler

# class TimedRoute(APIRoute):
#     def get_route_handler(self) -> Callable:
#         original_route_handler = super().get_route_handler()

#         async def custom_route_handler(request: Request) -> Response:
#             before = time.time()
#             # requests = request
#             # print(requests)
#             response: Response = await original_route_handler(request)
#             duration = time.time() - before
#             # response.headers["X-Response-Time"] = str(duration)
#             logs_path = os.path.join(os.path.dirname(
#                 os.path.realpath(__file__)), "..", "storage/logs/")
#             # print(jsonable_encoder(requests))
#             logger.add(
#                 "".join([logs_path, "api-{time:YYYY-MM-DD}.log"]),retention="10 days", rotation="100 MB")
#             headers = Headers(scope=request.scope)
#             content_type = headers.get("content-type")
#             if content_type in ["application/json", "charset=utf-8"] :
#                 payload = request.query_params if request.method == 'GET' else await request.json()
#                 logger.info("[REQUEST {} - {}] : {}", request.method, str(request.url), jsonable_encoder(payload))
#                 logger.info("[RESPONSE {} - {}] : {} duration {}", request.method, str(request.url),
#                         json.dumps(json.loads(response.body), indent=4), duration)
                
#             else:
#                 payload = request.query_params
#                 logger.info("[REQUEST {} - {}] : {}", request.method,
#                             str(request.url), jsonable_encoder(payload))
#                 logger.info("[RESPONSE {} - {}] : {} duration {}", request.method, str(request.url),
#                         json.dumps(json.loads(response.body), indent=4), duration)
#             return response

#         return custom_route_handler
