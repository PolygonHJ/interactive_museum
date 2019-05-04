#!/usr/bin/python3

import board
import neopixel

import threading
import time

from flask import Flask
from flask import render_template


app = Flask(__name__)

pixels = neopixel.NeoPixel(board.D18, 3)
rooms = [0, 0, 0]


# Setup the home page
@app.route('/')
def index():
    return render_template('index.html')


# Setup the room state toggling
@app.route('/room<int:room_number>')
def handle_request(room_number):
    # Room state is controlled independantly in javascript and python
    response = 'Room ' + str(room_number) + ' toggled'
    rooms[room_number - 1] = (( rooms[room_number - 1] + 1) % 2)
    
    # Turn the lights on and off
    for i in range(len(rooms)):
        pixels[i] = (50*rooms[i], 50*rooms[i], 50*rooms[i])
        
    return response, 200


# Draw the Path
def path():
    for i in range(len(rooms)):
        rooms[i] = 0
    print(rooms)
    pixels.fill((0, 0, 0))
    
    i = 0
    while not any(rooms):
        pixels[i] = (0, 50, 0)
        pixels[i-1] = (0, 0, 0)
        time.sleep(0.5)
        i += 1
        if ( i > 2 ): i = 0
    return


# Setup the path walking
@app.route('/path')
def handle_path():
    pixels.fill((0, 0, 0))            
    path_thr = threading.Thread(target=path)
    path_thr.start()
    return 'Rainbow', 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
