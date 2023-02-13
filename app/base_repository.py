from datetime import datetime
from importlib import import_module
from typing import Union
from fastapi import HTTPException

import stringcase
from fastapi_pagination.paginator import paginate
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session

from .query_helper import QueryHelper
from .responses import HTTPResponse

class BaseRepository:
    model = None

    def __init__(self, class_model: str = None, model_instance: str = None):
        self.response = HTTPResponse()
        try:
            if class_model:
                if not model_instance:
                    model_instance = stringcase.pascalcase(class_model)
                self.model = getattr(import_module("app.models.{}".format(class_model)), model_instance)
                self.pk = getattr(self.model, str(inspect(self.model).primary_key[0]).split(".")[-1:][0])
                self.query_helper = QueryHelper(self.model, self.pk)
            else:
                self.query_helper = QueryHelper()
        except Exception as exc:
            raise HTTPException(status_code=500, detail=exc)

    def find(self, db: Session, filters: dict = None, sorts: dict = None):
        try:
            filter_columns = self.query_helper.filter_by(filters)
            sort_columns = self.query_helper.sort_by(sorts)
            result = db.query(self.model).filter(*filter_columns).order_by(*sort_columns).all()
            return paginate(result) if result else self.response.not_found()
        except Exception as exc:
            return self.response.server_error(exc, True)

    def find_one(self, db: Session, id: Union[int, str]):
        try:
            query = self.query_helper.set_query(db.query(self.model))
            if self.query_helper.exists(id):
                return query.filter(self.pk==id).first()
            return self.response.not_found("Resource not found (ID: {})".format(id))
        except Exception as exc:
            return self.response.server_error(exc, True)

    def store(self, db: Session, payload: dict):
        try:
            if hasattr(self.model, "createdAt"):
                payload.update({"createdAt": datetime.now()})
            if hasattr(self.model, "updatedAt"):
                payload.update({"updatedAt": datetime.now()})
            data = self.model(**payload)
            db.add(data)
            db.commit()
            db.refresh(data)
            return self.response.created(data, "Resource stored successfully")
        except Exception as exc:
            db.rollback()
            return self.response.server_error(exc, True)

    def update(self, db: Session, id: Union[int, str], payload: dict):
        try:
            query = self.query_helper.set_query(db.query(self.model))
            if self.query_helper.exists(id):
                if hasattr(self.model, "updatedAt"):
                    query.filter(self.pk==id).update({"updatedAt": datetime.now()})
                query.filter(self.pk==id).update(payload)
                db.commit()
                return self.response.accepted(query.filter(self.pk==id).first(), "Resource ID {} is updated".format(id))
            return self.response.not_found("Resource not found (ID: {})".format(id))
        except Exception as exc:
            db.rollback()
            return self.response.server_error(exc, True)

    def destroy(self, db: Session, id: Union[int, str]):
        try:
            query = self.query_helper.set_query(db.query(self.model))
            if self.query_helper.exists(id):
                if hasattr(self.model, "deletedAt"):
                    query.filter(self.pk==id).update({"deletedAt": datetime.now()})
                elif hasattr(self.model, "isActive"):
                    query.filter(self.pk==id).update({"isActive": False})
                else:
                    query.filter(self.pk==id).delete()
                db.commit()
                return self.response.no_content("Resource ID {} is deleted".format(id))
            return self.response.not_found("Resource not found (ID: {})".format(id))
        except Exception as exc:
            db.rollback()
            return self.response.server_error(exc, True)
