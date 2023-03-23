from fastapi import HTTPException, status
from fastapi_sqlalchemy import db
from models.user import Role as ModelRole
from models.user import User as ModelUser
from schemas.user import UserRegister
from utils.password_hashing import get_password_hash


def find_all_users():
    return_users = db.session.query(ModelUser).filter().all()
    return return_users


def get_user_by_username(username: str):
    return_user = db.session.query(ModelUser).filter(
        ModelUser.username == username).first()
    return return_user


async def add_user(user: UserRegister):
    added_user = ModelUser(**user.dict())

    existing_user = db.session.query(ModelUser).filter(
        ModelUser.username == user.username).first()
    if existing_user != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this username already exists!")
    existing_user = db.session.query(ModelUser).filter(
        ModelUser.email == user.email).first()
    if existing_user != None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this email already exists!")

    added_user.password = get_password_hash(added_user.password)
    client_role = db.session.query(ModelRole).filter(
        ModelRole.role == "STUDENT").first()
    added_user.roles.append(client_role)
    db.session.add(added_user)
    db.session.commit()
    return added_user
