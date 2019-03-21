import json
import connexion
import flask
import pandas
import statistics
from pandas.io.json import json_normalize
from airlines_api import orm

with open('airlines.json', 'r') as f:
	airlines = json.load(f)

HOST = 'localhost'
PORT = 5000


# serializes response data as json/csv depending on content-type in request header
def serialize(data):
	ctype = connexion.request.accept_mimetypes
	print(connexion.request.accept_mimetypes)
	if 'text/csv' in ctype:
		return flask.Response(pandas.io.json.json_normalize(data).to_csv(), content_type='text/csv')
	else:
		return data


def get_airports():
	data = []
	for item in airlines:
		in_data = False
		for i in data:
			if i['code'] == item['airport']['code']:
				in_data = True
				break
		if in_data is False:
			item['airport']['links'] = [
				{'rel': "Get airport carriers", 'href': HOST + str(PORT) + '/v1/airports/' + item['airport']['code'] + '/carriers'}]
			data.append(item['airport'])
	return serialize(data)


def get_carriers():
	data = []
	for item in airlines:
		in_data = False
		for i in data:
			if i['code'] == item['carrier']['code']:
				in_data = True
				break
		if in_data is False:
			data.append(item['carrier'])

	return serialize(data)


def get_airport_carriers(airport_code):
	data = []
	for item in airlines:
		if item['airport']['code'] == airport_code:
			data.append(item['carrier'])
	return serialize(data)


def get_statistics(carrier_code, airport, month=None):
	data = []
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item['airport']['code'] == airport:
				if item['time']['month'] == month:
					data.append(item['statistics'])
				elif month is None:
					data.append(item['statistics'])
	return serialize(data)


def post_statistics(request_body):
	# add new entry
	airlines.append(request_body)
	return []


# maybe change month to required here
def put_statistics(carrier_code, airport, request_body, month=None):
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item['airport']['code'] == airport:
				if item['time']['month'] == month:
					item = request_body
				elif month is None:
					item = request_body
	return []


def delete_statistics(carrier_code, airport, month=None):
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item['airport']['code'] == airport:
				if item['time']['month'] == month:
					del item
				elif month is None:
					del item
	return []


def get_flights(carrier_code, airport, month=None):
	data = []
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item['airport']['code'] == airport:
				if item['time']['month'] == month:
					data.append(item['statistics']['flights'])
				elif month is None:
					data.append(item['statistics']['flights'])
	return serialize(data)


def get_delays(carrier_specific=None, airport=None, month=None):
	data = []
	for item in airlines:
		if item['airport']['code'] == airport:
			if item['time']['month'] == month:
				if carrier_specific is None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])
			elif month is None:
				if carrier_specific is None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])
		elif airport is None:
			if item['time']['month'] == month:
				if carrier_specific is None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])
			elif month is None:
				if carrier_specific is None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])

	return serialize(data)


def get_delay_statistics(airport1, airport2, carrier_code=None, carrier_specific=None):
	data = []
	list = []
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item['airport']['code'] == airport1:
				list.append(item['statistics']['# of delays'][carrier_specific])
			if item['airport']['code'] == airport2:
				list.append(item['statistics']['# of delays'][carrier_specific])
		elif carrier_code is None:
			if item['airport']['code'] == airport1:
				list.append(item['statistics']['# of delays'][carrier_specific])
			if item['airport']['code'] == airport2:
				list.append(item['statistics']['# of delays'][carrier_specific])

	mean = statistics.mean(list)
	median = statistics.median(list)
	std = statistics.stdev(list)

	data = {"mean": mean, "median": median, "standard deviation": std}

	return serialize(data)


# db_session = orm.init_db('sqlite:///:memory:')
# orm.load_db(db_session, airlines)


app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=True)
