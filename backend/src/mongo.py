import pymongo

import config


client = pymongo.MongoClient(
    f"mongodb://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_HOST}:{config.MONGO_PORT}/"
)

db = client[config.MONGO_BASE]

col_articles = db["articles"]
col_diseases = db["diseases"]
col_employees = db["employees"]
