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

def user_put(user_data):   
    user_ref = db.collection('users').document(user_data.username)   #Set the name
    user_ref.set({'password': user_data.password})      #add the related password to that name
    

# the \ is to be able to use enter
def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()

def put_todo(user_id, description):
    todos_collection_ref = db.collection('users').document(user_id).collection('todos')
    todos_collection_ref.add({'description':description, 'done': False })  #Add the info to todo collection
    
def delete_todo(user_id, todo_id):
    todo_ref = _get_todo_ref(user_id,todo_id)
    #todo_ref = db.collection('users').document(user_id).collection('todos').document(todo_id)
    todo_ref.delete()
    
    
def update_todo(user_id, todo_id, done):
    
    if done=='False':
        todo_done = True
    else:
        todo_done = False
    
    #todo_done = not bool(done)

    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': todo_done})


def _get_todo_ref(user_id,todo_id):
    return db.document('users/{}/todos/{}'.format(user_id,todo_id))