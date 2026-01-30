import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# Base de datos local
# db_client = MongoClient().local.users

# Base de datos remota
db_client = MongoClient(os.environ.get("MONGODB_URI")).test.users