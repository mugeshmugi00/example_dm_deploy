from pymongo import MongoClient

local = MongoClient("mongodb+srv://mugi84219:mugesh2002@cluster0.3dld5.mongodb.net/mugesh_database")

db = local.mugesh_database

coll = db.admin_collection
