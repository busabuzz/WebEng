import json
import connexion
import flask
import pandas
import statistics
from flask_cors import CORS
from pandas.io.json import json_normalize

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
		in_data = False
		for i in data:
			if i['code'] == item['carrier']['code']:
				in_data = True
				break
		if in_data is False:
		    if item['airport']['code'] == airport_code:
			    data.append(item['carrier'])
	return serialize(data)


def get_statistics(carrier, airport, month=None, year=None):
	data = []
	for item in airlines:
		if item['carrier']['code'] == carrier:
			if item['airport']['code'] == airport:
				if item['time']['month'] == month or month is None:
					if item['time']['year'] == year or year is None:
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
					return {}, 200

	return {"error": "entry does not exist"}, 404


def delete_statistics(airport, carrier, year=None, month=None):
	for item in airlines:
		if item['carrier']['code'] == carrier:
			if item['airport']['code'] == airport:
				if item['time']['year'] == year or year is None:
					if item['time']['month'] == month or month is None:
						airlines[:] = [tup for tup in airlines if tup is not item]

	return {}, 200


def get_flights(carrier_code, airport, year=None, month=None):
	data = dict.fromkeys(airlines[0]['statistics']['flights'].keys(), 0)

	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item['airport']['code'] == airport:
				if item['time']['month'] == month or month is None:
					if item['time']['year'] == year or year is None:
						for key in data.keys():
							data[key] += item['statistics']['flights'][key]
	return serialize(data)


def get_delays(reasons=None, airport=None, year=None, month=None):
	data = {}
	carriers = []
	response = []
	for item in airlines:
		if item['carrier']['code'] not in carriers:
			carriers.append(item['carrier']['code'])

	for carr in carriers:
		data[carr] = 0

	for item in airlines:
		if airport is None or airport == item['airport']['code']:
			if month is None or month == item['time']['month']:
				if year is None or year == item['time']['year']:
					if reasons is None:
						for key, value in item['statistics']['minutes delayed'].items():
							data[item['carrier']['code']] += value
					else:
						for reason in reasons:
							data[item['carrier']['code']] += item['statistics']['minutes delayed'][reason]
	for key, value in data.items():
		response.append({'carrier': key, 'delay': value})
	return serialize(response)


def get_delay_statistics(airport1, airport2, carrier_code=None, reasons=None):
	""" returns descriptive statistics """
	car1 = []
	car2 = []
	car = []
	data = {}
	response = []

	if carrier_code is None:
		for item in airlines:
			if item['airport']['code'] == airport1 and airport1 not in car1:
				car1.append(item['carrier']['code'])
			if item['airport']['code'] == airport2 and airport2 not in car2:
				car2.append(item['carrier']['code'])

		for item in car1:
			for item2 in car2:
				if item == item2:
					car.append(item)
					data[item] = []
					break
	else:
		data[carrier_code] = []
		car.append(carrier_code)

	for item in airlines:
		if item['carrier']['code'] in car and (item['airport']['code'] == airport1 or item['airport']['code'] == airport2):

			data[item['carrier']['code']].append(item['statistics']['minutes delayed'])

	for key, value in data.items():
		entry = {'carrier': key, 'data': {}, 'statistics': {}}
		if reasons is None:
			for reason, dat in value[0].items():
				entry['data'][reason] = []
		else:
			for reason in reasons:
				entry['data'][reason] = []

		for item in value:
			for reason, dat in entry['data'].items():
				entry['data'][reason].append(item[reason])

		for reason, dat in entry['data'].items():
			entry['statistics'][reason] = {}
			entry['statistics'][reason]['mean'] = statistics.mean(entry['data'][reason])
			entry['statistics'][reason]['median'] = statistics.median(entry['data'][reason])
			entry['statistics'][reason]['stdev'] = statistics.stdev(entry['data'][reason])

		del entry['data']
		response.append(entry)

	return serialize(response)


app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')
CORS(app.app)

if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=True)
