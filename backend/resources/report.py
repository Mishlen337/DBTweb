from flask_restful import Resource, reqparse


class Report(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("name", type=str, required=True)
        parser.add_argument(
            "report_type", type=str, required=True
        )
        parser.add_argument(
            "text", type=str,  required=True
        )
        data = parser.parse_args()
        with open("./report.txt", 'w') as f:
            f.write(data)
        return {"message": "ок"}
