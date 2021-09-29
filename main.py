import pymongo

from pymongo import MongoClient
client = MongoClient()

client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

db = client.test_database

collection = db.test_collection

import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

db.list_collection_names()

import pprint
pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

posts.find_one({"author": "Eliot"})

post_id
pprint.pprint(posts.find_one({"_id": post_id}))

post_id_as_str = str(post_id)
posts.find_one({"_id": post_id_as_str}) # No result

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})