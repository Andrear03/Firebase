import firebase_admin
from firebase_admin import credentials, db

class FirebaseDB:
    def __init__(self):
       
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://andre-de7ac-default-rtdb.firebaseio.com/' 
        })
        self.ref = db.reference('/usuarios')  
    def insert_user(self, nombre, email, edad):
        user_id = self.ref.push().key  # Genera un ID único
        user_data = {
            "user_id": user_id,
            "nombre": nombre,
            "email": email,
            "edad": edad
        }
        self.ref.child(user_id).set(user_data)
        return user_id

    # Método para obtener la información de un usuario específico
    def get_user(self, user_id):
        user_data = self.ref.child(user_id).get()
        return user_data

    # Método para actualizar los datos de un usuario
    def update_user(self, user_id, nombre=None, email=None, edad=None):
        updates = {}
        if nombre:
            updates["nombre"] = nombre
        if email:
            updates["email"] = email
        if edad:
            updates["edad"] = edad
        self.ref.child(user_id).update(updates)

    # Método para eliminar un usuario de la base de datos
    def delete_user(self, user_id):
        self.ref.child(user_id).delete()