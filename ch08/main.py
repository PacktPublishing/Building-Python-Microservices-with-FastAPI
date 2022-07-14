from fastapi import FastAPI

from api import login, admin, vendor, customer, billing, messenger, publication, content, sales, subscription
from config.db.gino_db import db
app = FastAPI()

@app.on_event("startup")
async def initialize():
    engine = await db.set_bind("postgresql+asyncpg://postgres:admin2255@localhost:5433/nsms")

@app.on_event("shutdown")
async def destroy():
    engine, db.bind = db.bind, None
    await engine.close()
    
app.include_router(login.router, prefix='/ch08')
app.include_router(admin.router, prefix='/ch08')
app.include_router(vendor.router, prefix='/ch08')
app.include_router(customer.router, prefix='/ch08')
app.include_router(billing.router, prefix='/ch08')
app.include_router(messenger.router, prefix='/ch08')
app.include_router(publication.router, prefix='/ch08')
app.include_router(content.router, prefix='/ch08')
app.include_router(sales.router, prefix='/ch08')
app.include_router(subscription.router, prefix='/ch08')


