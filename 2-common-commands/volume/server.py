from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/book')
def json_file():
    file = open('./volume_data/book.json')
    json_data = json.load(file)
    return json_data

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
