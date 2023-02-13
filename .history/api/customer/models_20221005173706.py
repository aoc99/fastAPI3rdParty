from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sql_app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSON
import datetime, json, uuid

class conString(Base):
    __tablename__ = "connections"

    id = Column(Integer(), primary_key=True)
    moduleCode = Column('module_code', Integer())
    url = Column(String(100))
    secretKey = Column('secret_key', Integer())
    aliasName = Column('alias_name', String(150))
