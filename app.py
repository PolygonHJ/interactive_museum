#!/usr/bin/python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/room<int:room_number>', methods=["GET"])
def handle_request(room_number):
    # Room state is controlled independantly in javascript and python
    response = 'Room ' + str(room_number) + ' toggled'
    print(response)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
