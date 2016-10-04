## APIze

[![PyPI](https://img.shields.io/pypi/v/apize.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/status/apize.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/pyversions/apize.svg)](https://pypi.python.org/pypi/apize/)

Write quickly and easily to HTTP API clients.

### Installation

```bash
pip install apize
```

### Get started

#### Example with 1 API

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


#### Example with multiple API

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

### Apize class

```python
from apize.apize import Apize
```

Accept 2 args:
* api_url (__str__) : your url base (ex: https://myapi.com/api)
* ssl_cert (__str__ or __bool__) : your ssl cert file path (if necessary)

#### example
```python
from apize.apize import Apize

app = Apize('https://myapi.com/api')
## With auto-signed ssl cert and allowed verification.
app_https = Apize('https://myapi.com/api', ssl_cert='.cert/mycert')
```

### Call decorator

Accept 2 args:
* path (__str__) : requests path (ex: /foo/bar/)
* method (__str__) : http method (default: GET)

Your function must be decored by call decorator and must be return a dict.

Dict accept 5 args:
* data (__dict__ or __str__) : body request
* args (__dict__) : args to parse url (ex: /foo/:bar/)
* params (__dict__) : params in url (ex: ?id=12)
* headers (__dict__) : http headers 
* cookies (__dict__) : http cookies
* timout (__int__) : set a timeout for request (default: 8 seconds)
* is_json (__bool__) : define if data args must be parsed in json.
* ssl_cert (__bool__ or __str__) : override Apize.ssl_cert for special case (default: False)


#### example
```python
from apize.apize import Apize

app = Apize('https://myapi.com/api')

@app.call('/maps/:lat/:long/')
def get_map(key, zoom)
	args = {'lat': '47.331881, 'long': '5.032221,12'}
	params = {'zoom': 12}
	
	## Final url : 
	## https://myapi.com/api/maps/47.331881/5.032221,12/?zoom=12
	
	return {'args': args, 'params': params}
```

### Use multiple API

```python
from apize.decorators import apize_raw
```

Use apize_raw decorator (same as call decorator but without Apize object).

#### example
```python
from apize.decorators import apize_raw

@apize_raw('https://myapi.com/api/maps/:lat/:long/')
def get_map(key, zoom)
	args = {'lat': '47.331881, 'long': '5.032221,12'}
	params = {'zoom': 12}
	
	## Final url : 
	## https://myapi.com/api/maps/47.331881/5.032221,12/?zoom=12
	
	return {'args': args, 'params': params}
```
