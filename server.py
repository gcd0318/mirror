from flask import Flask, jsonify, render_template
from weather import get_weather

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    data = get_weather()
    return render_template('index.html', data=data)

@app.route('/weather')
def weather():
    data = get_weather()
    return jsonify(data)


if '__main__' == __name__:
    app.run(host='0.0.0.0', port=8888, debug=True)
