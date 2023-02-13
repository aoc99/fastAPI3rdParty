from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi import BackgroundTasks
from app.config import Settings
from typing import Dict, List, Optional, Union
from fastapi.responses import ORJSONResponse


class HttpBaseResponse(ORJSONResponse):
    def __init__(self, data: Optional[Union[Dict, List]] = None, errors: Optional[List] = None, message: Optional[str] = None, meta: Optional[Dict] = None, status_code: int = 200, tasks: BackgroundTasks = None) -> None:
        if not meta:
            meta = {
                "currentPage": 0,
                "firstPage": 0,
                "lastPage": 0,
                "perPage": Settings.app_page_size,
                "totalPage": 0,
                "total": 0,
            }
        super().__init__(
            content=jsonable_encoder({
                "data": data,
                "errors": errors,
                "message": message,
                "meta": meta,
                "statusCode": status_code,
            }),
            status_code=200,
            background=tasks,
        )

# class HttpServerErrorResponse(JSONResponse):
#     def __init__(self, message: str, background: Optional[BackgroundTasks] = None) -> None:
#         super().__init__(
#             content=jsonable_encoder({
#                 "data": [],
#                 "errors": [],
#                 "message": message,
#                 "meta": empty_meta,
#                 "statusCode": 500,
#             }),
#             status_code=200,
#             background=background,
#         )

class HttpInternalServerErrorResponse(HttpBaseResponse):
    def __init__(self, errors: Optional[List], message: Optional[str] = "INTERNAL_SERVER_ERROR", tasks: BackgroundTasks = None) -> None:
        super().__init__(errors=errors, message=message, status_code=500, tasks=tasks)


class HttpMainResponse(ORJSONResponse):
    def __init__(self) -> None:
        super().__init__(
            content=jsonable_encoder({
                "name": Settings.app_name,
                "version": Settings.app_version
            }),
            status_code=200,
        )

class HTTPResponse:
    data: Optional[List] = None
    errors: Optional[str] = None
    message: str
    meta: Optional[dict] = None
    statusCode: int = 200

    def accepted(self, data, message = None) -> JSONResponse:
        self.data = data
        self.message = message
        self.statusCode = 201
        return self.__make_response()

    def bad_request(self, errors = None, message = None) -> JSONResponse:
        self.data = None
        self.errors = errors
        self.message = message
        self.statusCode = 400
        return self.__make_response()

    def conflict(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 409
        return self.__make_response()

    def created(self, data, message = None) -> JSONResponse:
        self.data = data
        self.message = message
        self.statusCode = 201
        return self.__make_response()

    def forbidden(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 403
        return self.__make_response()

    def found(self, message = None) -> JSONResponse:
        self.message = message
        self.statusCode = 302
        return self.__make_response()

    def method_not_allowed(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 405
        return self.__make_response()

    def no_content(self, message = None) -> JSONResponse:
        self.message = message
        self.statusCode = 204
        return self.__make_response()

    def not_acceptable(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 406
        return self.__make_response()

    def not_found(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 404
        return self.__make_response()

    def server_error(self, message = None, raise_exc: bool = False) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 500
        if raise_exc:
            raise HTTPException(status_code=self.statusCode, detail=self.message)
        return self.__make_response()

    def service_unavailable(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 503
        return self.__make_response()

    def success(self, data, message = None) -> JSONResponse:
        self.data = data
        self.message = message
        self.statusCode = 200
        return self.__make_response()

    def unauthorized(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 401
        return self.__make_response()

    def unsupported_media_type(self, message = None) -> JSONResponse:
        self.data = None
        self.message = message
        self.statusCode = 415
        return self.__make_response()

    def validation_error(self, errors, message = None) -> JSONResponse:
        self.data = None
        # self.errors = errors
        self.message = errors
        self.statusCode = 422
        return self.__make_response()

    def __make_response(self) -> JSONResponse:
        content = jsonable_encoder({"data": self.data, "errors": self.errors, "message": self.message, "meta": self.meta, "statusCode": self.statusCode})
        return JSONResponse(content=content, status_code=self.statusCode)
