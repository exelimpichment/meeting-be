from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    pass
