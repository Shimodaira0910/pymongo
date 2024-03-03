from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from business.service import DbService

app = FastAPI()
db_service = DbService()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get")
async def get_database_info():
    return db_service.get_user()

@app.post("/post")
async def post_user_data(request: Request):
    received_data = await request.json()
    result = db_service.regist_user(received_data)
    return result

@app.post("/update")
async def update_user_age(request: Request):
    received_data = await request.json()
    return db_service.regist_user(received_data)
    