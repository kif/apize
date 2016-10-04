#!/usr/bin/env python3

from apize.apize import Apize

app = Apize('https://www.google.com/recaptcha/api')


@app.call('/siteverify', method='POST')
def verify_response(private_key, response):
	'''
	https://developers.google.com/recaptcha/docs/verify
	'''
	data = {'secret': private_key, 'response': reponse}
	
	return {'data': data}
	

if __name__ == "__main__":
	response = verify_response('fehzbhz...', 'dajzdjaiz...')
	
	print(response['status'])
	print(response['data'])
