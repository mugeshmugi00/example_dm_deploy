from . import db
from bson import ObjectId

def findUser(userId):
    userObj_id = ObjectId(userId)
    user = db.coll.find_one({"_id":userObj_id})
    return user

def getuser(userId):
    return ObjectId(userId)