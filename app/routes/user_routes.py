from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.user_model import User

router = APIRouter()


@router.get("/list")
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users": users}
