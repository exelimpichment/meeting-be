from sqlalchemy import Column, String
from app.database.base import Base
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()), index=True)
    first_name = Column(String(255), index=True)
    last_name = Column(String(255), index=True)
