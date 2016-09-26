## APIze

### Installation

```bash
pip install apize
```

### Get started

```python
from apize.decorators import apize

API_KEY = 'hfbehbf...'
API = 'https://maps.googleapis.com/maps/api/place'


@apize(API + '/autocomplete/json?input=:input&key=:key&types=:types')
def autocomplete_place(entry):
	'''
	https://developers.google.com/places/web-service/autocomplete
	'''
	params = {
		'input': entry,
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

* params.
* data.
* headers.
* cookies.
* timeout (int), default 8 seconds.

Response __dict__:

* data:  body HTTPResponse (dict if is_json == True)
* content_type:  MIME types
* status:  status code HTTP
* is_json:  boolean
* timeout:  boolean (if requests.exceptions.Timeout is raised).

