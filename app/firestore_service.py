import firebase_admin
from firebase_admin import credentials  #Used to communicate
from firebase_admin import firestore


credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

#Now create instance of the class client 
db = firestore.client()

#To get the users list
def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

# the \ is to be able to use enter
def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()