from flask import Flask, jsonify
from weather import get_weather

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return 'mirror'

@app.route('/weather')
def weather():
    name, data = get_weather()
    return jsonify({name: data})


if '__main__' == __name__:
    app.run(host='0.0.0.0', port=8888, debug=True)
