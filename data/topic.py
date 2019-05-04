from pymongo import MongoClient
import utils.config as conf

client = MongoClient(**conf.db_location())
db_name, collection_name = conf.topic_collection()
collection = client.get_database(db_name).get_collection(collection_name)
