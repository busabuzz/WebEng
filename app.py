from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

app = Flask(__name__)
api = Api(app)


# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))
#
#
parser = reqparse.RequestParser()
# parser.add_argument('task')


with open('airlines.json', 'r') as f:
    data = json.load(f)
    print(data[0]['airport']['name'])


class Airports(Resource):
    def get(self):
        response_data = []
        for item in data:
            if item['airport'] not in response_data:
                response_data.append(item['airport'])

        return {'data': response_data}


class Carriers(Resource):
    def get(self):
        return 'Carriers'


class Carrier(Resource):
    def get(self, airport_code):
        return 'Carriers at specific airport'


class CarrierStatistics(Resource):
    def get(self, carrier_code, airport_code, month):
        return 'Flight statistics for given carrier, airport and month/all months'


class CarrierFlightTimings(Resource):
    def get(self, carrier_code, airport_code, month):
        return 'Number of on-time, delayed and canceled flights for a given carrier, airport and month/all months'


class CarrierDelays(Resource):
    def get(self, airport_code, month):
        return 'Number of minutes delay per carrier attributed to carrier-specific reasons/all reasons for a given' \
               ' month/all months and for a specific airport/all airports'


class CarrierDelayStatistics(Resource):
    def get(self):
        return 'descriptive statistics (mean, median, standard deviation) for carrier-specific delays (as above) for ' \
               'a flight between any two airports in the USA for a specific carrier/all carriers serving this route.'


# Actually setup the Api resource routing here
api.add_resource(Airports, '/airports')
api.add_resource(Carriers, '/carriers')
api.add_resource(Carrier, '/carrier')
api.add_resource(CarrierStatistics, '/carrier_statistics')
api.add_resource(CarrierFlightTimings, '/carrier_flight_timings')
api.add_resource(CarrierDelays, '/carrier_delays')
api.add_resource(CarrierDelayStatistics, '/carrier_delay_statistics')

if __name__ == '__main__':
    app.run(debug=True)
