#!/usr/bin/env python3

from apize.decorators import apize


API = 'https://www.google.com'

@apize(domain + '/recaptcha/api/siteverify', method='POST')
def verify_response(private_key, response):
	'''
	https://developers.google.com/recaptcha/docs/verify
	'''
	data = {"secret": private_key, "response": reponse}
	
	return {'data': data}
	

if __name__ == "__main__":
	response = verify_response('fehzbhz...', 'dajzdjaiz...')
	
	print(response['status'])
	print(response['data'])
