from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse 
from starlette.exceptions import HTTPException as GlobalStarletteHTTPException
from fastapi.exceptions import RequestValidationError
from handler_exceptions import PostFeedbackException, PostRatingException
from fastapi.responses import JSONResponse

from admin import manager
from login import user
from feedback import post
from places import destination
from tourist import visit
from datetime import datetime


app = FastAPI()

app.include_router(manager.router)
app.include_router(user.router)
app.include_router(destination.router)
app.include_router(visit.router)
app.include_router(
    post.router,
    prefix="/ch02/post"
)

@app.middleware("http")
async def log_transaction_filter(request: Request, call_next):
    start_time = datetime.now()
    method_name= request.method
    qp_map = request.query_params
    pp_map = request.path_params
    with open("request_log.txt", mode="a") as reqfile:
        content = f"method: {method_name}, query param: {qp_map}, path params: {pp_map} received at {datetime.now()}"
        reqfile.write(content)
    response = await call_next(request)
    process_time = datetime.now() - start_time
    response.headers["X-Time-Elapsed"] = str(process_time)
    return response

@app.get("/ch02")
def index():
    return {"message": "Intelligent Tourist System Prototype!"}

@app.exception_handler(PostFeedbackException)
def feedback_exception_handler(req: Request, ex: PostFeedbackException):
    
    return JSONResponse(
        status_code=ex.status_code,
        content={"message": f"error: {ex.detail}"}
        )
    
@app.exception_handler(PostRatingException)
def rating_exception_handler(req: Request, ex: PostRatingException):
        return JSONResponse(
        status_code=ex.status_code,
        content={"message": f"error: {ex.detail}"}
        )

@app.exception_handler(GlobalStarletteHTTPException)
def global_exception_handler(req: Request, ex: str):
    return PlainTextResponse(f"Error message: {ex}", status_code=400)


@app.exception_handler(RequestValidationError)
def validationerror_exception_handler(req: Request, ex: str):
    return PlainTextResponse(f"Error message: {ex}", status_code=400)