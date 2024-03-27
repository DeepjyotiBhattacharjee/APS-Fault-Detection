
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://deepjyotibhattacharjee217:Snape1993@cluster0.eiomi4b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

database = client['Dummydb']

collection = database['Products']

d = {
    "companyName":"Accenture",
    "product":"Sensor Fault Predictor",
    "price": 2900,
}

res = collection.insert_one(d)

all_record = collection.find()

for idx,record in enumerate(all_record):
    print(f"{idx} : {record}")