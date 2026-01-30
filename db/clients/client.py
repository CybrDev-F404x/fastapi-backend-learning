from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local.users

# Base de datos remota
db_client = MongoClient("mongodb+srv://test:del1al9@clusterfastapi.v1zluv0.mongodb.net/?appName=ClusterFastAPI").test.users