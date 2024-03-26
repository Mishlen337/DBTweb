import json
import pymongo
from datetime import datetime
from loguru import logger

import config


client = pymongo.MongoClient(
    f"mongodb://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_HOST}:{config.MONGO_PORT}/"
)

db = client[config.MONGO_BASE]

col_articles = db["articles"]
col_diseases = db["diseases"]
col_employees = db["employees"]

col_articles.create_index([("title", pymongo.ASCENDING)], unique=True)
col_diseases.create_index([("description", pymongo.ASCENDING)], unique=True)
col_employees.create_index([("fio", pymongo.ASCENDING)], unique=True)


if config.RESTORE_DIR.exists():
    try:
        with open(config.RESTORE_DIR.joinpath('articles.json'), 'r') as f:
            data = list(json.load(f))
            for d in data:
                d.pop('_id')
                d["created"] = datetime.fromisoformat(d["created"]["$date"])
            col_articles.insert_many(data)
            logger.info('articles restored!')
    except Exception as ex:
        logger.warning(f"Can't restore articles from files {str(ex.__str__())[:100]}")
    
    try:
        with open(config.RESTORE_DIR.joinpath('diseases.json'), 'r') as f:
            data = json.load(f)
            for d in data:
                d.pop('_id')
            col_diseases.insert_many(data)
            logger.info('diseases restored!')
    except Exception as ex:
        logger.warning(f"Can't restore diseases from files {str(ex)[:100]}")
    
    try:
        with open(config.RESTORE_DIR.joinpath('employees.json'), 'r') as f:
            data = json.load(f)
            for d in data:
                d.pop('_id')
            col_employees.insert_many(data)
            logger.info('employees restored!')
    except Exception as ex:
        logger.warning(f"Can't restore employees from files {str(ex)[:100]}")
