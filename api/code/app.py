import time

from flask import Flask

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def hello_world():
    return 'Welcome to RUI application!</a>'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}


if __name__ == '__main__':
    app.run(debug=True, port=5000,  host='0.0.0.0')
