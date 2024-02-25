import logging

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# import config
from resources.employee import Employee
from resources.article import Article
from resources.diseases import Disease
from resources.recommendation import Recommendation
from resources.report import Report

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Employee, "/employees")
api.add_resource(Article, "/articles")
api.add_resource(Disease, "/diseases")
api.add_resource(Recommendation, "/recommendation")
api.add_resource(Report, "/report")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777, debug=True)
