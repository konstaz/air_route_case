import os
import pymongo


class Database(object):

    URI = os.getenv('MONGO_URI')
    DATABASE = None

    @staticmethod
    def initialize():

        client = pymongo.MongoClient(
            Database.URI
        )
        Database.DATABASE = client[os.getenv('MONGO_NAME')]


    @staticmethod
    def save_one_to_db(data):
        return Database.DATABASE[f"{os.getenv('MONGO_COLLECTION')}"].insert_one(data)
        
    @staticmethod
    def load_one_from_db(query):
        return Database.DATABASE[f"{os.getenv('MONGO_COLLECTION')}"].find_one(query)

    @staticmethod
    def update_one_to_db(_id, data):
        return Database.DATABASE[f"{os.getenv('MONGO_COLLECTION')}"].update_one({'_id': _id}, {"$set": data})

    @staticmethod
    def remove_one_from_db(_id):
        return Database.DATABASE[f"{os.getenv('MONGO_COLLECTION')}"].delete_one({'_id': _id})

    @staticmethod
    def load_routes_from_db(query):
        return Database.DATABASE[f"{os.getenv('MONGO_COLLECTION')}"].find(query)
