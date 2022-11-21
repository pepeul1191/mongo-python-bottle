from pymongo import MongoClient

database_name = 'demo'
client = MongoClient('mongodb://localhost:27019/')
db = client[database_name]
