from fastapi import FastAPI
from api import book, buyer, buyer_async, cart, receipt, order, login, profile, purchase, reference

app = FastAPI()
app.include_router(purchase.router, prefix="/ch06")
app.include_router(buyer.router, prefix="/ch06")
app.include_router(buyer_async.router, prefix="/ch06")
app.include_router(receipt.router, prefix="/ch06")
app.include_router(order.router, prefix="/ch06")
app.include_router(cart.router, prefix="/ch06")
app.include_router(login.router, prefix="/ch06")
app.include_router(profile.router, prefix="/ch06")
app.include_router(book.router, prefix="/ch06")
app.include_router(reference.router, prefix="/ch06")