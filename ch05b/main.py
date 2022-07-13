from fastapi import FastAPI

from api import login, attendance

app = FastAPI()
app.include_router(login.router, prefix='/ch05')
app.include_router(attendance.router, prefix='/ch05')

