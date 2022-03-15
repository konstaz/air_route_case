import os
import pymongo


class Database(object):

    # URI = os.getenv('mongodb://localhost:27017/')
    URI = 'mongodb://localhost:27017/'
    DATABASE = None

    @staticmethod
    def initialize():
        print(f'POOOOOOOOO :::::: {os.getenv("MONGO_NAME")}')
        print(f'POOOOOOOOO :::::: {os.getenv("MONGO_COLLECTION")}')
        client = pymongo.MongoClient(
            # f'mongodb://{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}/{os.getenv("MONGO_NAME")}'
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
