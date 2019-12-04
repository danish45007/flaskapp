from pymongo import MongoClient
from werkzeug.security import generate_password_hash


client = MongoClient("mongodb+srv://danish:danish12@chatapp-onqho.mongodb.net/test?retryWrites=true&w=majority")

chat_db = client.get_database("chatdb")
user_collection = chat_db.get_collection("users")

def save_user(username,email,password):
    password_hash = generate_password_hash(password)
    user_collection.insert_one({'_id':username,'email':email,'password':password_hash})

save_user("danish","danish45007@gmail.com","danish12")


def getuser(username):
    user_data = user_collection.find_one({'_id':username})
    return User(user_data['_id'],user_data['email'],user_data['password']) if user_data else None
