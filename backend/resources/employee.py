import base64
from copy import deepcopy
from bson.objectid import ObjectId
from werkzeug.datastructures import FileStorage
from flask_restful import Resource, reqparse, inputs

from config import token
from src.mongo import col_employees

class Employee(Resource):
    def get(self):
        employees = list(col_employees.find({}))
        sorted_employees = sorted(employees, key=lambda x: x["fio"])
        for se in sorted_employees:
            se["_id"] = str(se["_id"])

        return {"message": "ok", "employees": sorted_employees}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("fio", type=str, location="form", required=True)
        parser.add_argument("specialization", type=str, action='append', location="form", required=True)
        parser.add_argument("education", type=str, action='append', location="form", required=True)
        parser.add_argument("workExperience", type=str, action='append', location="form", required=True)
        parser.add_argument(
            "imageSrc", type=FileStorage, location="files", required=True
        )
        parser.add_argument("appointmentLink", type=str, location="form", required=True)
        parser.add_argument(
            "isPopular", type=inputs.boolean, location="form", required=True
        )
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        del data["token"]
        data["imageSrc"] = base64.b64encode(data["imageSrc"].read()).decode("utf-8")

        col_employees.insert_one(data)
        return {"message": "ок"}

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=str, location="form", required=True)
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        id = data.pop("id")
        result = col_employees.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return {"message": "ок"}

        return {"message": "No such employee"}, 404

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=str, location="form", required=True)
        parser.add_argument("fio", type=str, location="form", required=False)
        parser.add_argument("specialization", type=str, action='append', location="form", required=False)
        parser.add_argument("education", type=str, action='append', location="form", required=False)
        parser.add_argument("workExperience", type=str, action='append', location="form", required=False)
        parser.add_argument(
            "imageSrc", type=FileStorage, location="files", required=False
        )
        parser.add_argument("appointmentLink", type=str, location="form", required=False)
        parser.add_argument(
            "isPopular", type=inputs.boolean, location="form", required=False
        )
        data = parser.parse_args()

        patch_fields = ["fio", "specialization", "education", "workExperience", "appointmentLink", "isPopular"]

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

        result = col_employees.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count == 1:
            return {"message": "ок"}

        return {"message": "No such employee"}, 404
