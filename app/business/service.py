from db.db import MongoDbManager

class DbService:
    
    def __init__(self) -> None:
        self._db_manager = MongoDbManager()
        
    def get_user(self) -> str:
        _users_data = self._db_manager.get_user_list()
        users_data = []
        for i in _users_data.values():
            users_data.append(i)        
        return users_data
    
    def regist_user(self, received_data):
        return self._db_manager.register_user_data(received_data)
    
    def update_user(self, received_data):
        user_name = received_data['username']
        update_age = received_data['age']    
        return self._db_manager.update_user_age(user_name, update_age)