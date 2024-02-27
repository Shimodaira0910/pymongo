from starlette.requests import Request
from pymongo import MongoClient
from dotenv import load_dotenv
from os.path import join, dirname
import os

load_dotenv(verbose=True)
dotenv_path = join(dirname(dirname(__file__)), '.env')
load_dotenv(dotenv_path)

class MongoDbManager:
    
    def __init__(self) -> None:
        self._collection = self._connect_db()
    
    def _connect_db(self) -> MongoClient:
        username = os.environ.get("MONGO_USERNAME")
        password = os.environ.get("MONGO_PASSWORD")
        hostname = os.environ.get("MONGO_HOSTNAME")
    
        client = MongoClient(f'mongodb://{username}:{password}@{hostname}:27017/')
        db = client['myDataBase']
        return db['testCollection']
    
    def get_user_list(self) -> dict:
        data = list(self._collection.find({}, {'_id': 0}))
        return {"data": data}
    
    def register_user_data(self, received_data) -> dict:
        self._collection.insert_one(received_data)
        return{"insert": "OK!"}
    
    def update_user_age(self, received_data) -> dict:
        user_name = received_data['username']
        update_age = received_data['age']    
        update_user = self._collection.find_one({'username': user_name})

        if update_user is None or update_user == "":
            return {"warn":"Userが存在しません!"}
        else:
            self._collection.update_one({'username': user_name}, {'$set':{'age': update_age}})
            result = self._collection.find_one({}, {'_id': 0})
            return {'result': result}