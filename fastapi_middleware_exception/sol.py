from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse  

app = FastAPI() 

class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=400,
        content={"message": f"Custom error occurred: {exc.name}"},
    )

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url.path}")
    response = await call_next(request)
    print(f"Response: {response.status_code}")
    return response

@app.get("/hello")
async def read_root():
    return {"message": "Hello, Welcome to FastAPI!"}

@app.get("/{path:path}")
async def catch_all(path: str):
    raise CustomException(name="Invalid endpoint")



