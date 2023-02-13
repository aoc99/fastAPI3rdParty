from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional, Union
from app.config import Settings

class MainResponse(BaseModel):
    name: str
    version: str

class FilterAttributes(BaseModel):
    field: str
    value: Optional[Any]
    type: str = "string"
    comparator: str = "="

class SortAttributes(BaseModel):
    field: str
    sort: str = "desc"

class QueryRequest(BaseModel):
    filters: Optional[List[FilterAttributes]]
    sorts: Optional[List[SortAttributes]]
    page: int = 1
    perPage: int = Field(default=Settings.app_page_size, title="Per Page",)

class MetaAttributes(BaseModel):
    currentPage: int = Field(default=0, title="Current Page")
    firstPage: int = Field(title="First Page")
    lastPage: int = Field(title="Last Page")
    perPage: int = Field(default=Settings.app_page_size, title="Per Page")
    totalPage: int = Field(default=0, title="Total Page")
    total: int = Field(default=0,)

class BaseResponse(BaseModel):
    data: Optional[Union[Dict, List]] = []
    errors: Optional[List] = None
    message: Optional[str] = None
    meta: MetaAttributes
    statusCode: int

class AcceptedResponse(BaseResponse):
    statusCode: int = 202

class BadRequestResponse(BaseResponse):
    statusCode: int = 400

class BadGatewayResponse(BaseResponse):
    statusCode: int = 502

class ConflictResponse(BaseResponse):
    statusCode: int = 202

class CreatedResponse(BaseResponse):
    statusCode: int = 201

class ForbiddenResponse(BaseResponse):
    statusCode: int = 403

class FoundResponse(BaseResponse):
    statusCode: int = 302

class InternalServerErrorResponse(BaseResponse):
    statusCode: int = 500

class MethodNotAllowedResponse(BaseResponse):
    statusCode: int = 405

class MovedPermanentlyResponse(BaseResponse):
    statusCode: int = 301

class NotAcceptableResponse(BaseResponse):
    statusCode: int = 406

class NoContentResponse(BaseResponse):
    statusCode: int = 204

class NotFoundResponse(BaseResponse):
    statusCode: int = 404

class PreconditionFailedResponse(BaseResponse):
    statusCode: int = 419

class ProxyAuthenticationRequiredResponse(BaseResponse):
    statusCode: int = 407

class ServiceUnavailableResponse(BaseResponse):
    statusCode: int = 503

class SuccessResponse(BaseResponse):
    statusCode: int = 200

class TooManyRequestsResponse(BaseResponse):
    statusCode: int = 429

class UnauthorizedResponse(BaseResponse):
    statusCode: int = 401

class UnsupportedMediaTypeResponse(BaseResponse):
    statusCode: int = 415

class ValidationErrorsResponse(BaseResponse):
    statusCode: int = 422
