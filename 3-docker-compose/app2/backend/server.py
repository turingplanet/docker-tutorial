from flask import Flask, render_template
import redis
import os
REDIS_HOST = os.environ.get('REDIS_HOST', '0.0.0.0')

app = Flask(__name__)
cache = redis.Redis(host = REDIS_HOST, port = 6379, db = 0)
cache.set('hits', 0)

@app.route('/')
def get_data():
    hit_num = cache.incr('hits')
    return f'I have been seen {hit_num} times.\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
