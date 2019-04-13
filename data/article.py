from pymongo import MongoClient
import utils.config as conf

client = MongoClient(**conf.db_location())
db_name, collection_name = conf.article_collection()
collection = client.get_database(db_name).get_collection(collection_name)


def find(aid):
    if aid is None:
        return None
    else:
        return collection.find_one({"_id": aid})


def save(d: dict):
    result = collection.replace_one({'_id': d['_id']},
                                    d,
                                    upsert=True)
    print("update: ", result.modified_count)


def next_id():
    max_idx = -1
    for doc in collection.find({}, {'_id': 1}):
        max_idx = max(doc['_id'], max_idx)
    return max_idx + 1
