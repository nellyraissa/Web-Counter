import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_reload_count():
    retries = 5
    while True:
	try:
	    return cache.incr('Hits')
	except redis.exceptions.ConnectionError as exc:
	    if retries == 0:
		raise exc
	    retries -=1
	    time.sleep(0.250)

@app.route('/')

def greetings():
    count = get_reload_count()
    return ''Holla! we have hit {} times.\n'.format(count)
