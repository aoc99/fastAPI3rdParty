import os
import json
import importlib
from fastapi import Depends, FastAPI
from dependencies import get_query_token, get_token_header
from internal import admin
from sql_app.database import engine
# from api.gateway import models
from app.routes import router

from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
apm = make_apm_client(
    {'SERVICE_NAME': 'middleware', 'SERVER_URL': 'http://10.6.226.246:8200', 'ENVIRONMENT': 'development', 'GLOBAL_LABELS': 'platform=DemoPlatform, application=DemoApplication'
     })
app.add_middleware(ElasticAPM, client=apm)

app.include_router(router)

for curr_dir, _, files in os.walk("./api"):
    if "controller.py" in files:
        api_module = curr_dir.replace("./", "").replace("/", ".")
        module_name = api_module.split(".")[-1]
        route_module = importlib.import_module(api_module + ".controller", module_name)
        app.include_router(route_module.router)