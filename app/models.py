from .database import Base
import uuid
from sqlalchemy import Boolean, Column, ForeignKey, String


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()), index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
