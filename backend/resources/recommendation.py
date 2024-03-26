import base64
from loguru import logger
from flask_restful import Resource, reqparse

from src.mongo import col_employees
from config import recommendation_pipe, translation_pipe


def choose_specialist(predicted_field, specialists_priorities, thresh=0.5):
    field = predicted_field['label']
    score = predicted_field['score']
    if score < thresh:
        return None
    related_specialists = []
    for spec in specialists_priorities:
        if field in spec["priorities"].keys():
            related_specialists.append((spec["employee"], spec["priorities"][field]))
    sorted_related_specialists = sorted(related_specialists, key=lambda x: x[1])

    if sorted_related_specialists:
        return sorted_related_specialists[0][0]
    return None


eng_to_ru = {
    'depression': 'депрессия', 
    'anxiety': 'тревожность', 
    'bipolar disorder': 'биполярное расстройство', 
    'schizophrenia': 'шизофрения', 
    'PTSD': 'ПТСР', 
    'OCD': 'ОКР', 
    'ADHD': 'СДВГ', 
    'autism': 'аутизм', 
    'eating disorder': 'расстройство пищевого поведения', 
    'personality disorder': 'расстройство личности', 
    'phobia': 'фобия'
}


class Recommendation(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("problem", type=str, location="args", required=True)
        data = parser.parse_args()

        eng_problem = translation_pipe(data["problem"])[0]['translation_text']
        recommended_area = recommendation_pipe(eng_problem)[0]
        # recommended_area = "depression"
        employees = list(col_employees.find({}))
        specialists_priorities = []
        for em in employees:
            if em["area"]:
                specialists_priorities.append({"employee": em, "priorities": {ar: i for i, ar in enumerate(em["area"])}})

        employee = choose_specialist(recommended_area, specialists_priorities)
        if not employee:
            logger.info(f"no such employee for the area {recommended_area}")
            return {"message": "no such employee for the problem"}, 404
        employee["_id"] = str(employee["_id"])
        return {"message": "ok", "employee": dict(employee), "recommendedSpecialization": eng_to_ru[recommended_area['label']]}
