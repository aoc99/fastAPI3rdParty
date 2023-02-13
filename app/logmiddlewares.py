import gzip
from logging import Logger
from starlette.datastructures import FormData, Headers, UploadFile
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp, Message
from typing import Union
from app.helpers import json_pretty
from app.responses import HttpInternalServerErrorResponse


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, log: Logger) -> None:
        super().__init__(app)
        self._log = log

    async def payload_request(self, request: Request) -> None:
        _payload = await request._receive()

        async def receive_payload() -> Message:
            return _payload

        request._receive = receive_payload

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Union[Response, HttpInternalServerErrorResponse]:
        payload = None

        try:
            client = request.client
            http_method = request.method
            url = request.url
            log_text = f"[REQUEST] {client} {http_method} {url}"
            await self.payload_request(request)

            headers = Headers(scope=request.scope)
            content_type = headers.get("content-type")
            print(headers)

            if content_type:
                if "multipart/form-data" in content_type:
                    payload = []
                    _payload = await request.form()
                    for _key in _payload:
                        if isinstance(_payload[_key], UploadFile):
                            payload.append((_key, _payload[_key].filename))
                        else:
                            payload.append((_key, _payload[_key]))
                    log_text = log_text + f"\n{FormData(payload)}"
                elif "application/x-www-form-urlencoded" in content_type:
                    payload = await request.form()
                    log_text = log_text + f"\n{payload}"
                elif content_type == "application/json":
                    payload = await request.json()
                    log_text = log_text + f"\n{json_pretty(payload)}"

                self._log.info(log_text)
                response = await call_next(request)
                status_code = response.status_code
                log_text = f"[RESPONSE] {client} {http_method} {url} - HTTP Status Code {status_code}"

                if status_code != 204:
                    response_payload = response.body_iterator
                    if response_payload:
                        payload = b"".join([chunk async for chunk in response_payload])
                        headers = response.headers
                        content_type = headers.get("content-type")
                        if "content-encoding" in headers and content_type == "application/json":
                            payload = gzip.decompress(payload).decode("utf-8")
                        if content_type == "application/json":
                            log_text = log_text + f"\n{json_pretty(payload)}"
                        if "content-encoding" in headers and content_type == "application/json":
                            payload = gzip.compress(payload.encode("utf-8"), 9)
                else:
                    payload = None

                
                self._log.info(log_text)
                return Response(
                    content=payload,
                    headers=response.headers,
                    status_code=status_code,
                    media_type=response.media_type,
                    background=response.background
                )
            return await call_next(request)
        except Exception as exc:
            exception = str(exc)
            self._log.error(exception)
            return HttpInternalServerErrorResponse(exception)
