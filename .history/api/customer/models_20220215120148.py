from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sql_app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSON
import datetime, json, uuid

class Region(Base):
    __tablename__ = "regions"

    code = Column(Integer(), primary_key=True)
    parentCode = Column('parent_code', Integer())
    name = Column(String(100))
    regionType = Column('region_type', Integer())
