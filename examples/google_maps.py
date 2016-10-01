#!/usr/bin/env python3

from apize.decorators import apize

API_KEY = 'hfbehbf...'
API = 'https://maps.googleapis.com/maps/api/place'


@apize(API + '/autocomplete/json')
def autocomplete_place(query):
	'''
	https://developers.google.com/places/web-service/autocomplete
	'''
	params = {
		'input': query,
		'key': API_KEY,
		'types': '(cities)'
	}
	
	return {'params': params}



@apize(API + '/add/json', method='POST')
def add_place():
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
	params = {'key': API_KEY}

	return {'data': data, 'params': params}


if __name__ == "__main__":
	response = add_place()
	
	print(response['status'])
	print(response['data'])
	
	response = autocomplete_place('Par')
	
	print(response['status'])
	print(response['data'])
