## APIze

[![PyPI](https://img.shields.io/pypi/v/apize.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/status/apize.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/pyversions/apize.svg)](https://pypi.python.org/pypi/apize/)

Write quickly and easily to API clients.

### Installation

```bash
pip install apize
```

### Get started

#### If your script use 1 API, use __Apize__ class:

```python
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
```


#### If your script use multiple APIs, use apize_raw decorator:

```python
from apize.decorators import apize_raw

api_recaptcha = 'https://www.google.com/recaptcha/api'


@apize_raw(api_recaptcha + '/siteverify', method='POST')
def verify_response(private_key, response):
	'''
	https://developers.google.com/recaptcha/docs/verify
	'''
	data = {'secret': private_key, 'response': reponse}
	
	return {'data': data}


@apize_raw('http://mafreebox.free.fr/api_version')
def get_api_config():
	'''
	http://dev.freebox.fr/sdk/os/
	'''
	return {}


if __name__ == "__main__":
	resp1 = verify_response('fehzbhz...', 'dajzdjaiz...')
	resp2 = get_api_config()
```


Documentation in preparation ...

