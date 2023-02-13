from xxlimited import Str
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sql_app.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSON
import datetime, json, uuid

class Customer():
    __tablename__ = "customers"
    __return_keys__ = ["_id", "phoneNumber", "dob",
                       "name", "profilePicture", "useBiometric"]

    _id = Column("id", UUID(as_uuid=True), primary_key=True)
    phoneNumber = Column("phone_number", String(15))
    passcode = Column(String(255), nullable=True)
    name = Column(String(100), nullable=True)
    dob = Column(datetime(), nullable=True)
    profilePicture = Column("profile_picture", String(), nullable=True)
    useBiometric = Column("use_biometric",Boolean(), nullable=True)
    deviceId = Column("device_id", String(80))
    os = Column("device_os", String(3))
    deviceProperties = Column("device_properties", JSON())
    failedPasscode = Column("failed_passcode", nullable=False, default=0)
    createdAt = Column("created_at", datetime,
                          nullable=True, default=datetime.datetime.now())
    updatedAt = Column("updated_at", datetime,
                          nullable=True, default=datetime.datetime.now())
    isDeleted = Column("is_deleted", Boolean(), nullable=False)
    isDeletedAt = Column("is_deleted_at", datetime,
                            nullable=True, default=datetime.datetime.now())
