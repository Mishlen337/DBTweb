import base64
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage

from config import token
from src.mongo import col_diseases

diseases = [
    {
        "id": 1,
        "description": "Отчаянные попытки предотвратить реальное или воображаемое одиночество",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl1.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 2,
        "description": "Повторяющиеся нестабильные и интенсивные межличностные отношения",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl2.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 3,
        "description": "Временные параноидальные идеи, связанные со стрессом",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl3.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 4,
        "description": "Расстройство идентичности: выраженная и стойкая нестабильность самооценки",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl4.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 5,
        "description": "Импульсивность как минимум в двух областях, потенциально способных нанести вред",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl5.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 6,
        "description": "Повторяющиеся суицидальные мысли, угрозы суицида",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl6.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 7,
        "description": "Аффективная нестабильность",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl7.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 8,
        "description": "Хроническое чувство пустоты",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl8.jpg", "rb").read()
        ).decode("utf-8"),
    },
    {
        "id": 9,
        "description": "Неуместный сильный гнев или трудности с контролем ярости или гнева",
        "imageSrc": base64.b64encode(
            open("./assets/diseases/prl9.jpg", "rb").read()
        ).decode("utf-8"),
    },
]


class Disease(Resource):
    def get(self):
        diseases = list(col_diseases.find({}))
        for ar in diseases:
            ar["_id"] = str(ar["_id"])
        return {"message": "ok", "diseases": diseases}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("description", type=str, location="form", required=True)
        parser.add_argument(
            "imageSrc", type=FileStorage, location="files", required=True
        )
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        del data["token"]
        data["imageSrc"] = base64.b64encode(data["imageSrc"].read()).decode("utf-8")

        col_diseases.insert_one(data)
        return {"message": "ок"}

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=str, location="form", required=True)
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        id = data.pop("id")
        result = col_diseases.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"message": "ок"}

        return {"message": "No such disease"}, 404

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=str, location="form", required=True)
        parser.add_argument("description", type=str, location="form", required=False)
        parser.add_argument(
            "imageSrc", type=FileStorage, location="files", required=False
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

        result = col_diseases.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count == 1:
            return {"message": "ок"}

        return {"message": "No such disease"}, 404
