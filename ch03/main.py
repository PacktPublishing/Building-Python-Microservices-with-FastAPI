from fastapi import FastAPI, Depends

from api import recipes, users, posts, login, admin, keywords, admin_mcontainer, complaints
from dependencies.global_transactions import log_transaction

app = FastAPI(dependencies=[Depends(log_transaction)])

app.include_router(recipes.router, prefix="/ch03")
app.include_router(users.router, prefix="/ch03")
app.include_router(posts.router, prefix="/ch03")
app.include_router(login.router, prefix="/ch03")
app.include_router(admin.router, prefix="/ch03")
app.include_router(keywords.router, prefix="/ch03")
app.include_router(admin_mcontainer.router, prefix="/ch03")
app.include_router(complaints.router, prefix="/ch03")

@app.get("/ch03")
def index():
    return {"message": "Cooking Recipe Rating Prototype!"}