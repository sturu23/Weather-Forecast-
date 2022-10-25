from flask_restx import Api, Resource, reqparse
from app.routes.parse.parsed_data_for_api import parsed_data_for_api


api = Api(doc='/api/', prefix='/api')


@api.route("/weather-forecast/<city>")
class Weather(Resource):
    def get(self,city):

        return parsed_data_for_api(city), 200
