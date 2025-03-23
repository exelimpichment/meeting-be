from sqlalchemy import Column, String, Date
from app.database.base import Base
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()), index=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    date_of_birth = Column(Date)
