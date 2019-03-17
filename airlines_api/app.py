import csv
import json
import flask_csv
import connexion
import flask

from airlines_api import orm

with open('airlines.json', 'r') as f:
    airlines = json.load(f)


def serialize(data):
    return data


def get_airports():
    print(connexion.request.content_type)
    airport_list = [item['airport'] for item in airlines]
    airport_list = airport_list[0:10]
    for item in airport_list:
        item['links'] = [{'rel': "Get airport carriers", 'href': 'localhost:5000/airports/'+item['code']+'/carriers'}]
    return serialize(airport_list)


def get_carriers():
    data = []
    for item in airlines:
        if item not in data:
            data.append(item['carrier'])
            if len(data) > 9:
                break
    return serialize(data)


def get_airport_carriers(airport_code):
    data = []
    for item in airlines:
        if item['airport']['code'] == airport_code:
            data.append(item['carrier'])
            if len(data) > 9:
                break

    return serialize(data)


def get_statistics(carrier_code, airport, month=None):
    return []


def post_statistics(carrier_code):
    return []


def put_statistics(carrier_code):
    return []


def delete_statistics(carrier_code):
    return []


def get_flights(carrier_code, airport, month=None):
    return []


def get_delays(carrier_specific=False, airport=None, month=None):
    return []


def get_delay_statistics(carrier_specific=None, airport=None, month=None):
    return []


db_session = orm.init_db('sqlite:///:memory:')
orm.load_db(db_session, airlines)


app = connexion.App(__name__, specification_dir='./')


# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

