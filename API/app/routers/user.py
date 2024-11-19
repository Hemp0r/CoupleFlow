# app/routers/user.py
from app.dependencies import get_db, get_password_generator
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    password_generator=Depends(get_password_generator),
):
    # Check if the email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password and create the user
    hashed_password = password_generator.hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
