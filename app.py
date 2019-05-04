#!/usr/bin/python3

import board
import neopixel
from time import sleep

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

    # Turn the lights on and off
    for i in range(len(rooms)):
        pixels[i] = (50*rooms[i], 50*rooms[i], 50*rooms[i])
    
    return response, 200


@app.route('/path')
def handle_path():
    # Turn the lights on and off
    for i in range(len(rooms)):
        pixels[i] = (50, 0, 0)
        pixels[i-1] = (0, 0, 0)
        sleep(1)
    
    return 'Rainbow', 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
