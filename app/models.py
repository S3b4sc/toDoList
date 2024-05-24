from flask_login import UserMixin
from .firestore_service import get_user  #Tp make the query


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin):
    '''
        We extend the class, UserMixin, whcih has the minimun reqirements to
        implement user_loader
        
        It receives an object of the class UserData
    '''
    
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password
            
    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dict()['password']
        )
        #Now, we have the data, we can create the model
        
        return UserModel(user_data)