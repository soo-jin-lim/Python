from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)

print(client.list_databases_names())