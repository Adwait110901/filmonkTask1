from pymongo import MongoClient


mongodb_url = "mongodb://localhost:27017"

client = MongoClient(mongodb_url, 8000)

db = client["filmonk"]
collection = db.filmonkCollection


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "aadhar_id": user["aadhar_id"],
        "email": user["email"],
        "age":user["age"]
    }
     
async def add_user(user_data : dict)->dict:
    user =  collection.insert_one(user_data)
    new_user =  collection.find_one({"_id":user.inserted_id})
    return user_helper(new_user)


async def get_Users():
    users=[]
    for user in collection.find():
        users.append(user_helper(user))
    return users



    