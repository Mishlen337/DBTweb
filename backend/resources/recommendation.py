import base64
from loguru import logger
from flask_restful import Resource, reqparse

employee = {
    "id": 1,
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
    "is_popular": True,
}
specialization = "когнитивно-поведенческий терапевт"

class Recommendation(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("problem", type=str, location="args", required=True)
        data = parser.parse_args()

        logger.info(f"Problem: {data['problem']}")
        return {"message": "ok", "employee": employee, "specialization": specialization}
