from flask import Flask, jsonify, render_template
from weather import get_weather
from air import get_air

import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

conf_root = '/etc/mirror/'

@app.route('/')
def index():
    weather = get_weather(conf_root + 'weather.conf')
    air = get_air(conf_root + '/air.conf')
    return render_template('main.html', weather=weather, air=air)

@app.route('/weather')
def weather():
    data = get_weather(conf_root + 'weather.conf')
    return jsonify(data)

@app.route('/weather/<i>')
def weather_i(i):
    data = get_weather(conf_root + 'weather.conf', int(i))
    return jsonify(data)

@app.route('/air')
def air():
    data = get_air(conf_root + 'air.conf')
    return jsonify(data)

@app.route('/admin')
def admin():
    return render_template('admin.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=8888, debug=True)
