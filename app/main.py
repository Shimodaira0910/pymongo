from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
from db.db import MongoDbManager

app = FastAPI()
mongo_manager = MongoDbManager()

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
    return mongo_manager.get_user_list()

@app.post("/post")
async def post_user_data(request: Request):
    received_data = await request.json()
    result = mongo_manager.register_user_data(received_data)
    return result

#TODO エラー
@app.post("/update")
async def update_user_age(request: Request):
    received_data = await request.json()
    return mongo_manager.update_user_age(received_data)