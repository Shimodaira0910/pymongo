from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
from os.path import join, dirname
import os

app = FastAPI()

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
def get_database_info():
    db = get_database()
    collection_name = db['testCollection']
    insert_data = {"name":"John", "age":"999"}
    collection_name.insert_one(insert_data)
    
    print(list(collection_name.find()))
    return {"test":"ok!"}
    