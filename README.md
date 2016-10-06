# APIze

[![PyPI](https://img.shields.io/pypi/v/apize.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/status/apize.svg)](https://pypi.python.org/pypi/apize/)
[![PyPI](https://img.shields.io/pypi/pyversions/apize.svg)](https://pypi.python.org/pypi/apize/)

Write quickly and easily to HTTP API clients.

## Installation

```bash
pip install apize
```

## Get started

### Apize class

```python
from apize.apize import Apize
```

Accept 3 args:
* api_url (__str__) : your url base (ex: https://myapi.com/api)
* headers (__dict__) : http headers (for any API requests)
* verify_cert (__bool__ or __str__) : disable SSL cert verification or get certfile path. (default True)

#### example
```python
from apize.apize import Apize

app = Apize('https://myapi.com/api')
## With auto-signed ssl cert and allowed verification.
app_https = Apize('https://myapi.com/api', verify_cert='/path/to/certfile')
```

### Call decorator

Accept 2 args:
* path (__str__) : requests path (ex: /foo/bar/)
* method (__str__) : http method (default: GET)

Your function must be decorated by call method and must be return a dict.

Dict may contain 8 elements:
* data (__dict__ or __str__) : body request
* args (__dict__) : args to parse url (ex: /foo/:bar/)
* params (__dict__) : params in url (ex: ?id=12)
* headers (__dict__) : override Apize.headers for special case
* cookies (__dict__) : http cookies
* timout (__int__) : set a timeout for request (default: 8 seconds)
* is_json (__bool__) : define if data args must be parsed in json.
* verify_cert (__bool__ or __str__) : override Apize.verify_cert for special case


#### example
```python
from apize.apize import Apize

app = Apize('https://myapi.com/api')

@app.call('/maps/:lat/:long/')
def get_map(key, zoom)
	args = {'lat': '47.331881', 'long': '5.032221'}
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
	args = {'lat': '47.331881', 'long': '5.032221'}
	params = {'zoom': 12}
	
	## Final url : 
	## https://myapi.com/api/maps/47.331881/5.032221,12/?zoom=12
	
	return {'args': args, 'params': params}
```

more examples in __examples/__ directory.
