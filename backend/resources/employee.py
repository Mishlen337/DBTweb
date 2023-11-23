import base64
from flask_restful import Resource, reqparse, inputs
from werkzeug.datastructures import FileStorage
from datetime import datetime
from copy import deepcopy

from config import token

employees = [
    {
        "id": 1,
        "fio": "Макарова Яна",
        "specialization": [
            "клинический психолог",
            "нейробиолог",
            "когнитивно-поведенческий",
            "диалектико – поведенческий терапевт",
        ],
        "education": [
            "2008 - 2013 гг. - РГГУ, Институт психологии им.Л.С.Выготского",
            "2010 г. - Боткинская больница, кафедра нейрохирургии, г. Москва",
            "2012-2013 гг. - Психиатрическая клиническая больница №1 им Н.А. Алексеева, г. Москва",
            "2015 - 2017 гг. - СПбГУ, факультет биологии, специализация 'Нейробиология, психофизиология', г. Санкт - Петербург",
            "2017-2020 гг. - СЗГМУ им. И.И. Мечникова, повышение квалификации по направлениям «Когнитивно-поведенческая терапия», «Когнитивно-поведенческая терапия пар», г. Санкт – Петербург",
            "2021 г. – Центр Когнитивной Терапии, повышение квалификации по направлению «Терапия, сфокусированная на сострадании», г. Москва",
            "2021 г. - Доктор Дуглас Туркингтон (Dr.Douglas Turkington, Royal College of Psychiatrists): 'Когнитивно-поведенческая терапия психозов",
            "с 2021г. - член коллегии Ассоциации клинического психоанализа и психотерапии, участник регулярной интервизионной группы",
        ],
        "workExperience": [
            "2013-2015 гг. – Психиатрическая клиническая больница №1 им.Н.А.Алексеева, г. Москва",
            "2015 – 2020 гг. – Психоневрологический диспансер №5 г. Санкт-Петербург",
            "2020 г. – по настоящее время - Частная практика",
        ],
        "imageSrc": base64.b64encode(
            open("./assets/employees/Makarova.jpg", "rb").read()
        ).decode("utf-8"),
        "appointmentLink": "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        "isPopular": False,
    },
    {
        "id": 2,
        "fio": "Головаха Николай",
        "specialization": [
            "К.М.Н.",
            "психотерапевт",
            "когнитивно-поведенческий терапевт",
            "диалектико–поведенческий терапевт",
        ],
        "education": [
            "1998 г. - Алтайский государственный медицинский университет по специальности лечебное дело",
            "Ординатура по специальности психиатрия-наркология.",
            "Кандидат медицинских наук.",
            "Сертификат врача психотерапевта",
            "Когнитивно-поведенческая терапия",
            "Диалектическая поведенческая терапия в Behavioral Tech под руководством André Ivanoff, PhD",
            "Участвовал в международных стажировках и конференциях по лечению ожирения, лечению расстройств пищевого поведения, помощи людям с суицидальным поведением и самоповреждениями",
        ],
        "workExperience": [
            "Кандидат медицинских наук",
            "Сертификат врача психотерапевта",
        ],
        "imageSrc": base64.b64encode(
            open("./assets/employees/Golovaha.jpg", "rb").read()
        ).decode("utf-8"),
        "appointmentLink": "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        "isPopular": True,
    },
    {
        "id": 3,
        "fio": "Mariia Aarseth",
        "specialization": [
            "Клинический психолог",
            "преподаватель",
            "психологии",
        ],
        "education": [
            "2009 г - Санкт-Петербургский институт гуманитарного образования, специальность - психолог",
            "2020 г - Санкт-Петербургский Межотраслевой Институт Повышения Квалификации, специальность - Клиническая психология",
        ],
        "workExperience": [
            "EMDR терапевт с Европейской аккредитацией ( как взрослый, так и детский ), супервизор.",
            "Член ассоциаций Норвегия, Россия, Казахстан.",
            "TFP ( терапия сфокусированная на переносе Columbia University Weill Cornell Medical CollegeOtto Friedmann Kernberg",
            "Обучение в Heidelberg University Germany. Martin Bohus, а так же Universitetet i Oslo Lars Mehlum. DBT, DBT PTSD, CFT",
        ],
        "imageSrc": base64.b64encode(
            open("./assets/employees/Aarseth.jpg", "rb").read()
        ).decode("utf-8"),
        "appointmentLink": "https://n269840.yclients.com/company/262333/select-services?o=m772221",
        "isPopular": True,
    },
]


class Employee(Resource):
    def get(self):
        sorted_employees = sorted(deepcopy(employees), key=lambda x: x["fio"])
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

        data["id"] = len(employees)
        data["imageSrc"] = base64.b64encode(data["imageSrc"].read()).decode("utf-8")

        # TODO Append data in bd
        employees.append(data)
        return {"message": "ок"}

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=int, location="form", required=True)
        data = parser.parse_args()

        if data["token"] != token:
            return {"message": "Access is denied"}, 403

        # TODO Remove data in bd
        for ind, ar in enumerate(employees):
            if ar["id"] == data["id"]:
                employees.pop(ind)
                return {"message": "ок"}

        return {"message": "No such employee"}, 404

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, location="form", required=True)
        parser.add_argument("id", type=int, location="form", required=True)
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

        # TODO Update data in bd
        for ind, ar in enumerate(employees):
            if ar["id"] == data["id"]:
                # update fields
                for field in patch_fields:
                    if data[field]:
                        employees[ind][field] = data[field]

                # update image
                if data["imageSrc"]:
                    employees[ind]["imageSrc"] = base64.b64encode(
                        data["imageSrc"].read()
                    ).decode("utf-8")
                return {"message": "ок"}

        return {"message": "No such employee"}, 404
