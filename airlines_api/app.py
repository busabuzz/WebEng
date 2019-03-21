import json
import connexion
import flask
import pandas
from pandas.io.json import json_normalize
from airlines_api import orm

with open('airlines.json', 'r') as f:
    airlines = json.load(f)


# serializes response data as json/csv depending on content-type in request header
def serialize(data):
    if connexion.request.content_type == 'text/csv':
        return flask.Response(pandas.io.json.json_normalize(data).to_csv(), content_type='text/csv')
    else:
        return data


def get_airports():
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
	data = []
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item ['airport']['code'] == airport:
				if item ['time']['month'] == month:
					data.append(item['statistics'])
				elif month == None:
					data.append(item['statistics'])
	return serialize(data)


def post_statistics(carrier_code):
    return []


def put_statistics(carrier_code):
    return []


def delete_statistics(carrier_code):
    return []


def get_flights(carrier_code, airport, month=None):
	data = []
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item ['airport']['code'] == airport:
				if item ['time']['month'] == month:
					data.append(item['statistics']['flights'])
				elif month == None:
					data.append(item['statistics']['flights'])
	return serialize(data)


def get_delays(carrier_specific=None, airport=None, month=None):
	data = []
	for item in airlines:
		if item['airport']['code'] == airport:
			if item['time']['month'] == month:
				if carrier_specific == None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])
			elif month == None:
				if carrier_specific == None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])
		elif airport == None:
			if item['time']['month'] == month:
				if carrier_specific == None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])
			elif month == None:
				if carrier_specific == None:
					data.append(item['statistics']['minutes delayed'])
				else:
					data.append(item['statistics']['minutes delayed'][carrier_specific])
	
	return serialize(data)


def get_delay_statistics(airport1, airport2, carrier_code=None, carrier_specific=None):
	data1 = []
	data2 = []
	innerdata1 = []
	innerdata2 = []
	for item in airlines:
		if item['carrier']['code'] == carrier_code:
			if item['airport']['code'] == airport1:
				innerdata1.append(item['carrier'])
				innerdata1.append(item['statistics']['# of delays'][carrier_specific])
				data1.append(innerdata1)
			if item['airport']['code'] == airport2:
				innderdata2.append(item['carrier'])
				innderdata2.append(item['statistics']['# of delays'][carrier_specific])
				data2.append(innerdata1)
		elif carrier_code == None:
			if item['airport']['code'] == airport1:
				innerdata1.append(item['carrier'])
				innerdata1.append(item['statistics']['# of delays'][carrier_specific])
				data1.append(innerdata1)
			if item['airport']['code'] == airport2:
				innerdata2.append(item['carrier'])
				innerdata2.append(item['statistics']['# of delays'][carrier_specific])
				data2.append(innerdata2)
	
	# Data1 and data2 now hold a json object with a string and a integer
	# Extract the integer from both objects and calculate mean, medium and std dev.
	# mean(data1[carrier_specific],data2[carrier_specific])
	# medium(data1[carrier_specific],data2[carrier_specific])
	# std(data1[carrier_specific],data2[carrier_specific])
	# add this to a new json object.
	return serialize(data1)


# db_session = orm.init_db('sqlite:///:memory:')
# orm.load_db(db_session, airlines)


app = connexion.App(__name__, specification_dir='./')


# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

