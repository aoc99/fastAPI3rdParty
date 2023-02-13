import datetime
from api.auth.models import ParameterUser, ParameterUrl
from sql_app.database_session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

class validate:
    def validateToken(db: Session = Depends(get_db), isvalidate=False):
        if isvalidate:
            dateTimeFormat = "%Y-%m-%d %H:%M:%S"
            now = datetime.datetime.strptime(
                datetime.datetime.now().strftime(dateTimeFormat), dateTimeFormat)
            getToken = db.query(ParameterUser).first()
            expiredAt = datetime.datetime.strptime(
                getToken.updated_at.strftime(dateTimeFormat), dateTimeFormat)
            isInInterval = (
                now - expiredAt).total_seconds() <= float(3600)
            return isInInterval
