import pymongo
import certifi


con_str = "mongodb+srv://FSDI_Ch30:Mongo_DB@cluster0.hiatpex.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db=client.get_database("OrganikaStore")

