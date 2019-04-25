#!/usr/bin/python3

import board
import neopixel

from flask import Flask
from flask import render_template


app = Flask(__name__)

pixels = neopixel.NeoPixel(board.D18, 3)
rooms = [0, 0, 0]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/room<int:room_number>')
def handle_request(room_number):
    # Room state is controlled independantly in javascript and python
    response = 'Room ' + str(room_number) + ' toggled'
    rooms[room_number - 1] = (( rooms[room_number - 1] + 1) % 2)
    
    lit = [x for x in range(len(rooms)) if (rooms[x])]
    print(lit)

    
    
    return response, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
