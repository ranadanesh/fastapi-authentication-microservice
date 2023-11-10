import httpx
from fastapi import APIRouter, HTTPException

from starlette import status
from .jwt import create_refresh_token, create_access_token
from .settings import port, mongodb_uri
# from db import collection
from .schemes import *

router = APIRouter(tags=["home/"])


@router.post('/signup', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate):

    async with httpx.AsyncClient() as client:
        response = await client.post(f'http://127.0.0.1:8001/user/create', json=user.model_dump())
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Credentials!!!')

        # return {"message": "OK"}
        return response.json()


@router.post('/login', status_code=status.HTTP_200_OK)
async def login(user: UserLogin):
    async with httpx.AsyncClient() as client:
        response = await client.post(f'http://127.0.0.1:8001/login', json=user.model_dump())
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Credentials!!!')

        access_token = create_access_token(user.username)
        refresh_token = create_refresh_token(user.username)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }


