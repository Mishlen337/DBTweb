import base64
from loguru import logger
from copy import deepcopy
from datetime import datetime
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse, inputs
from werkzeug.datastructures import FileStorage

from config import token
from src.mongo import col_articles


articles = [
    {
        "id": 1,
        "title": "История DBT терапии",
        "author": "Головаха Николай",
        "description": "Диалектическая поведенческая терапия (DBT) – создана Маршей Линехан во второй половине 20 века, для людей ...",
        "imageSrc": base64.b64encode(
            open("./assets/articles/article1.jpg", "rb").read()
        ).decode("utf-8"),
        "articleLink": "https://telegra.ph/Istoriya-DBT-terapii-10-21",
        "isPopular": True,
        "created": datetime.now(),
    },
    {
        "id": 2,
        "title": "Биосоциальная модель ПРЛ",
        "author": "Головаха Николай",
        "description": "Людям с ПРЛ сложно контролировать свои эмоции. Почему так происходит? Есть биологическая основа ...",
        "imageSrc": base64.b64encode(
            open("./assets/articles/article2.jpg", "rb").read()
        ).decode("utf-8"),
        "articleLink": "https://telegra.ph/Biosocialnaya-model-pogranichnogo-10-21",
        "isPopular": True,
        "created": datetime.now(),
    },
    {
        "id": 3,
        "title": "Эмоциональная дисрегуляция при ПРЛ",
        "author": "Головаха Николай",
        "description": "В ДБТ считается, что не умение регулировать сильные эмоции, приводит к проблемному поведению. Это такое поведение ...",
        "imageSrc": base64.b64encode(
            open("./assets/articles/article3.jpg", "rb").read()
        ).decode("utf-8"),
        "articleLink": "https://telegra.ph/EHmocionalnaya-disregulyaciya-pri-PRL-10-21",
        "isPopular": True,
        "created": datetime.now(),
    },
    {
        "id": 4,
        "title": "Возможности ДБТ при лечении ПРЛ",
        "author": "Головаха Николай",
        "description": "Мы не можем изменить повышенную врожденную эмоциональность. При этом, можно учиться регулировать свои эмоции с помощью  ...",
        "imageSrc": base64.b64encode(
            open("./assets/articles/article4.jpg", "rb").read()
        ).decode("utf-8"),
        "articleLink": "https://telegra.ph/Vozmozhnosti-DBT-pri-lechenii-PRL-10-21",
        "isPopular": False,
        "created": datetime.now(),
    },
]


class Article(Resource):
    def get(self):
        articles = list(col_articles.find({}))
        sorted_articles = sorted(articles, key=lambda x: x["created"])
        for ar in sorted_articles:
            ar["_id"] = str(ar["_id"])
            ar["created"] = ar["created"].isoformat()
        return {"message": "ok", "articles": sorted_articles}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("title", type=str, location="form", required=True)
        parser.add_argument("author", type=str, location="form", required=True)
        parser.add_argument("description", type=str, location="form", required=True)
        parser.add_argument(
            "imageSrc", type=FileStorage, location="files", required=True
        )
        parser.add_argument("articleLink", type=str, location="form", required=True)
        parser.add_argument(
            "isPopular", type=inputs.boolean, location="form", required=True
        )
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        del data["token"]
        data["imageSrc"] = base64.b64encode(data["imageSrc"].read()).decode("utf-8")
        data["created"] = datetime.now()

        col_articles.insert_one(data)
        return {"message": "ок"}

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=str, location="form", required=True)
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        id = data.pop("id")
        result = col_articles.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"message": "ок"}

        return {"message": "No such article"}, 404

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=str, location="form", required=True)
        parser.add_argument("title", type=str, location="form", required=False)
        parser.add_argument("author", type=str, location="form", required=False)
        parser.add_argument("description", type=str, location="form", required=False)
        parser.add_argument(
            "imageSrc", type=FileStorage, location="files", required=False
        )
        parser.add_argument("articleLink", type=str, location="form", required=False)
        parser.add_argument(
            "isPopular", type=inputs.boolean, location="form", required=False
        )
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        del data["token"]
        id = data.pop("id")

        update_data = {key: value for key, value in data.items() if value is not None}

        # update image
        if "imageSrc" in update_data:
            data["imageSrc"] = base64.b64encode(
                data["imageSrc"].read()
            ).decode("utf-8")

        result = col_articles.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count == 1:
            return {"message": "ок"}

        return {"message": "No such article"}, 404
