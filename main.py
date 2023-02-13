import os
import json
import importlib
from fastapi import Depends, FastAPI
from dependencies import get_query_token, get_token_header
from internal import admin
from sql_app.database import engine
# from app.routes import router
from app.routes import load_routes
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM
from app.config import Settings
from app.logging import Logging
from app.logmiddlewares import LoggingMiddleware
from loguru import logger
from app.config import Settings

app = FastAPI()

settings = Settings

# app.include_router(router)
# models.Base.metadata.create_all(bind=engine)
# apm = make_apm_client(
#     {'SERVICE_NAME': 'api-digitalSignature', 'SERVER_URL': 'http://192.168.232.232:8200', 'ENVIRONMENT': 'development', 'GLOBAL_LABELS': 'platform=DemoPlatform, application=DemoApplication'
#      })

app.logger = logger
app.settings = Settings

# app.add_middleware(ElasticAPM, client=apm)
# logging = Logging()
# logger = logging.log
# app.add_middleware(LoggingMiddleware, log=logger)
# load_routes(app)

for curr_dir, _, files in os.walk("./api"):
    if "controller.py" in files:
        api_module = curr_dir.replace("./", "").replace("/", ".")
        module_name = api_module.split(".")[-1]
        route_module = importlib.import_module(
            api_module + ".controller", module_name)
        # print(route_module)
        app.include_router(route_module.router)
