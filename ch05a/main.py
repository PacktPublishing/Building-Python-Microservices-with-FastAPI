from fastapi import FastAPI

from api import admin, members, trainers, login



app = FastAPI()
app.include_router(admin.router, prefix='/ch05')
app.include_router(members.router, prefix='/ch05')
app.include_router(trainers.router, prefix='/ch05')
app.include_router(login.router, prefix='/ch05')
