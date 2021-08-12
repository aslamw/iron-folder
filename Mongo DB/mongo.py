import pymongo as mg

myclient =  mg.MongoClient('mongodb://localhost:27017/')
mydb = myclient["mydatabase"]
mycol = mydb['customers']

#print(myclient.list_database_names())  ------ retorna uma lista dos bancos de dados do seu sistema
print(mydb.list_collection_names())
