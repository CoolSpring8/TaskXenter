from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from app.models.pydantic.user import User, UserIn, UserInDB, Token
from app.models.tortoise.user import User_DB
from app.api.dependencies.authentication import authenticate_user, create_access_token, get_current_user, get_password_hash

ACCESS_TOKEN_EXPIRE_MINUTES = 7*24*60  # a week

router = APIRouter()

@router.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/me', response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get('/register')
async def create_new_user(user_in:UserIn):
    hashed_password = get_password_hash(user_in.password)
    await User_DB.create(
        username = user_in.username,
        hashed_password = hashed_password
    )
    return {"success": True}
