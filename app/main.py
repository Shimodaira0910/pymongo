from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from dotenv import load_dotenv
from os.path import join, dirname
from fastapi.encoders import jsonable_encoder
import os

app = FastAPI()

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

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def get_database():
    username = os.environ.get("MONGO_USERNAME")
    password = os.environ.get("MONGO_PASSWORD")
    hostname = os.environ.get("MONGO_HOSTNAME")
    
    client = MongoClient(f'mongodb://{username}:{password}@{hostname}:27017/')
    return client['mydatabase']

@app.get("/get")
async def get_database_info():
    db = get_database()
    collection_name = db['testCollection']
    insert_data = {"name":"John", "age":"999"}
    collection_name.insert_one(insert_data)
    
    # collection化したものは、強制的に_idがつくため、_idを除外する必要がある。
    data = list(collection_name.find({}, {'_id': 0}))
    return {"data": data}