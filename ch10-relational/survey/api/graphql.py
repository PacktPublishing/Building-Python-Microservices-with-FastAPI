from fastapi import APIRouter
from piccolo_api.crud.endpoints import PiccoloCRUD
from piccolo_api.fastapi.endpoints import FastAPIWrapper

from survey.tables import Login, Profile

router = APIRouter()

FastAPIWrapper(
    "/login/",
    router,
    PiccoloCRUD(Login, read_only=False),
)

FastAPIWrapper(
    "/profile/",
    router,
    PiccoloCRUD(Profile, read_only=False),
)