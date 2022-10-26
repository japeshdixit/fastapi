from jose import jwt, JWTError
from datetime import datetime, timedelta
from jose import JWTError, jwt
from requests import Session
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings
OAuth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login")  # endpoint of login request
# Secret Key for authentication
# Algorithm used for authentication  hs256
# Expiration time
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=(ALGORITHM))
    return encoded_jwt


def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id: str = payload.get("user_id")
        if id is None:
            raise credential_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credential_exception
    return token_data


def get_current_user(token: str = Depends(OAuth2_scheme), db: Session = Depends(database.get_db)):

    crednetials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail="Could not validate credentials", headers={"www-Authenticate": "Bearer"})
    token = verify_access_token(token, crednetials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
