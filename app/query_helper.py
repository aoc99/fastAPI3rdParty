from importlib import import_module
from typing import List, Union

import stringcase
from fastapi_pagination.bases import AbstractParams, RawParams

class BodyParams(AbstractParams):
    def __init__(self, payload):
        for _key, _value in payload.items():
            setattr(self, _key, _value)

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.length,
            offset=self.length * (self.page - 1),
        )

class QueryHelper:
    def __init__(self, model = None, pk = None):
        if model and pk:
            self.model = model
            self.pk = pk
            self.query = None

    def exists(self, id: Union[int, str]):
        filters = [self.pk==id]
        if hasattr(self.model, "deletedAt"):
            filters.append(self.model.deletedAt==None)
        if hasattr(self.model, "isActive"):
            filters.append(self.model.isActive==True)
        return self.query.filter(*filters).first()

    def filter_by(self, filters: Union[dict, list] = None):
        filter_columns = []
        filters_type = type(filters)
        if filters:
            if filters_type is dict:
                for _column, _value in filters.items():
                    if _value and hasattr(self.model, _column):
                        column = getattr(self.model, _column)
                        column_type = str(column.property.columns[0].type)
                        if column_type.find("VARCHAR") != -1:
                            filter_columns.append(column.ilike("%" + _value + "%"))
                        if column_type.find("INTEGER") != -1 or column_type.find("BOOLEAN") != -1:
                            filter_columns.append(column==_value)
            if filters_type is list:
                for _filter in filters:
                    columns = _filter.field.split(".")
                    column = self.__relation(columns)
                    if column:
                        _value = self.__value_type(_filter.value, _filter.type)
                        if _filter.operator == "=":
                            filter_columns.append(column == _value)
                        if _filter.operator == "!=":
                            filter_columns.append(column != _value)
                        if _filter.operator == ">":
                            filter_columns.append(column > _value)
                        if _filter.operator == "<":
                            filter_columns.append(column < _value)
                        if _filter.operator == ">=":
                            filter_columns.append(column >= _value)
                        if _filter.operator == "<=":
                            filter_columns.append(column <= _value)
                        if _filter.operator == "like":
                            filter_columns.append(column.ilike("%" + _value + "%"))
        return filter_columns

    def params_body(self, payload: dict = None):
        if payload and "page" in payload and "length" in payload:
            return BodyParams({"page": payload["page"], "length": payload["length"]})
        return None

    def set_query(self, db_query, model = None, pk = None):
        if model:
            self.model = model
        if pk:
            self.pk = pk
        self.query = db_query
        return self.query

    def sort_by(self, sorts: Union[dict, list] = None, sort_type: str = "asc") -> List:
        sort_columns = []
        sorts_type = type(sorts)
        if sorts:
            if sorts_type is dict:
                for _column, _sort_type in sorts.items():
                    if hasattr(self.model, _column):
                        column = getattr(self.model, _column)
                        sort_columns.append(column.asc() if _sort_type == "asc" else column.desc())
            if sorts_type is list:
                for _sort in sorts:
                    columns = _sort.field.split(".")
                    column = self.__relation(columns)
                    if column:
                        sort_columns.append(column.asc() if _sort.type == "asc" else column.desc())
        else:
            if hasattr(self.model, "createdAt"):
                sort_columns.append(self.model.createdAt.asc() if sort_type == "asc" else self.model.createdAt.desc())
            else:
                sort_columns.append(self.pk.asc() if sort_type == "asc" else self.pk.desc())
        return sort_columns

    def __import_relation(self, klass: str):
        snake_klass = stringcase.snakecase(klass)
        pascal_klass = stringcase.pascalcase(klass)
        return getattr(import_module("app.models.{}".format(snake_klass)), pascal_klass)

    def __join(self, model, relation: str):
        if hasattr(model, relation):
            self.query = self.query.join(getattr(model, relation))

    def __relation(self, columns: list):
        columns_size = len(columns)
        column_name = columns.pop(columns_size - 1)
        if columns_size < 2 and hasattr(self.model, column_name):
            column = getattr(self.model, column_name)
        else:
            relation_model = self.model
            for i, relation in enumerate(columns[0:columns_size - 1]):
                _next = i + 1
                if _next < (columns_size - 1) and columns[_next]:
                    _property = columns[_next]
                    if hasattr(relation_model, _property) == False:
                        relation_model = self.__import_relation(relation)
                    self.__join(relation_model, _property)
            relation = columns[-1]
            self.__join(self.model, relation)
            relation_model = self.__import_relation(relation)
            column = getattr(relation_model, column_name)
        return column

    def __value_type(self, value, type: str):
        if type == "int":
            value = int(value)
        elif type == "string":
            value = str(value)
        elif type == "float":
            value = float(value)
        return value
