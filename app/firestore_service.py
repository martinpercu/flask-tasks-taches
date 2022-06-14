import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password })


def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()


def put_todo(user_id, description):
    todos_collection_ref =  db.collection('users').document(user_id).collection('todos')
    todos_collection_ref.add({'description' : description, 'done' : False})
    


def delete_todo(user_id, todo_id):
    # todo_ref = db.collection('users').document(user_id).collection('todos').document(todo_id)
    # Lo de arriba es lo mismo que lo que está abajo    
    todo_ref = db.document('users/{}/todos/{}'.format(user_id, todo_id))
    todo_ref.delete()
    # Fijarse que el todo_ref ahora lo traemos direcot con la funcion _get_todo_ref linea 49
    # que se usa en el delete_todo que sigue
    

def update_todo(user_id, todo_id, done):
    todo_done = not bool(done)
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': todo_done})


def _get_todo_ref(user_id, todo_id):
    return db.document('users/{}/todos/{}'.format(user_id, todo_id))

