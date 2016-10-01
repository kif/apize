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

```python
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


if __name__ == "__main__":
	response = autocomplete_place('Par')
	
	print(response['status'])
	print(response['data'])
```

More examples on __examples/__ directory.

Argument __dict__ accept:

* params (params in url ex: ?v=10).
* args (args to parse in url ex: /solid/:rock).
* data.
* headers.
* cookies.
* timeout (int), default 8 seconds.
* is_json (boolean), if data must be convert to json.

Response __dict__:

* data:  body HTTPResponse (dict if is_json == True)
* cookies: CookieJAR object
* content_type:  MIME types
* status:  status code HTTP
* is_json:  boolean
* timeout:  boolean (if requests.exceptions.Timeout is raised).

