#!/usr/bin/env python3

from apize.apize import Apize

app = Apize('https://maps.googleapis.com/maps/api')


@app.call('/place/autocomplete/json')
def autocomplete_city(query):
	'''
	https://developers.google.com/places/web-service/autocomplete
	'''
	params = {
		'input': query,
		'key': key,
		'types': '(cities)'
	}
	
	return {'params': params}


@app.call('/place/add/json', method='POST')
def add_place(key):
	'''
	https://developers.google.com/places/web-service/add-place
	'''
	data = {
		"location": {
			"lat": -33.8669710,
			"lng": 151.1958750
		},
		"accuracy": 50,
		"name": "Google Shoes!",
		"phone_number": "(02) 9374 4000",
		"address": "48 Pirrama Road, Pyrmont, NSW 2009, Australia",
		"types": ["shoe_store"],
		"website": "http://www.google.com.au/",
		"language": "fr-FR"
	}
	params = {'key': key}

	return {'data': data, 'params': params}


if __name__ == "__main__":
	key = 'hfbehbf...'
	
	resp1 = add_place(key)
	resp2 = autocomplete_city('Dij', key)

