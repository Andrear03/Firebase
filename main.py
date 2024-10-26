from firebase_db import FirebaseDB

# Crear una instancia de la clase FirebaseDB
db = FirebaseDB()

# Crear un usuario en Firebase
user_id = db.insert_user("Carlos López", "carlos@example.com", 28)
print(f"Usuario creado con ID: {user_id}")
