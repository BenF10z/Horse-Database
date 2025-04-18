import pymongo
from dotenv import load_dotenv

load_dotenv()

myclient = pymongo.MongoClient("mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@maincluster.d2oiew4.mongodb.net/?retryWrites=true&w=majority&appName={CLUSTER_NAME}")

mydb = myclient["horse_database"]
mycol = mydb["horses"]

mydict = { "name": "Tokai Teio", "wins": 8, "sex": "horse", "track": "Turf" }

x = mycol.insert_one(mydict)
print(x.inserted_id)