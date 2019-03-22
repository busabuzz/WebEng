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


# serializes response data as json/csv depending on mime_type in request header
def serialize(data):
	if 'text/csv' in connexion.request.accept_mimetypes:
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


def get_statistics(carrier, airport, month=None):
	data = []
	for item in airlines:
		if item['carrier']['code'] == carrier:
			if item['airport']['code'] == airport:
				if item['time']['month'] == month:
					data.append(item['statistics'])
				elif month is None:
					data.append(item['statistics'])
	return serialize(data)


def post_statistics(request_body):
	# add new entry
	airlines.append(request_body)
	return {}, 200


# maybe change month to required here
def put_statistics(request_body):
	for item in airlines:
		if item['carrier']['code'] == request_body['carrier']['code']:
			if item['airport']['code'] == request_body['airport']['code']:
				if item['time']['label'] == request_body['time']['label']:
					item['statistics'] = request_body['statistics']
					break

	return {}, 200


def delete_statistics(request_body):
	for item in airlines:
		if item['carrier']['code'] == request_body['carrier']['code']:
			if item['airport']['code'] == request_body['airport']['code']:
				if item['time']['label'] == request_body['time']['label']:
					del item
					break
	return {}, 200


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
	innerdata = {}
	for item in airlines:
		innerdata["carrier"] = item['carrier']
		if item['airport']['code'] == airport:
			if item['time']['month'] == month:
				if carrier_specific is None:
					innerdata["delays"] = (item['statistics']['minutes delayed'])
					data.append(innerdata)
				else:
					innerdata["delays"] = (item['statistics']['minutes delayed'][carrier_specific])
					data.append(innerdata)
			elif month is None:
				if carrier_specific is None:
					innerdata["delays"] = (item['statistics']['minutes delayed'])
					data.append(innerdata)
				else:
					innerdata["delays"] = (item['statistics']['minutes delayed'][carrier_specific])
					data.append(innerdata)
		elif airport is None:
			if item['time']['month'] == month:
				if carrier_specific is None:
					innerdata["delays"] = (item['statistics']['minutes delayed'])
					data.append(innerdata)
				else:
					innerdata["delays"] = (item['statistics']['minutes delayed'][carrier_specific])
					data.append(innerdata)
			elif month is None:
				if carrier_specific is None:
					innerdata["delays"] = (item['statistics']['minutes delayed'])
					data.append(innerdata)
				else:
					innerdata["delays"] = (item['statistics']['minutes delayed'][carrier_specific])
		innerdata = {}
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


app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=True)
