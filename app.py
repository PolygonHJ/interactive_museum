#!/usr/bin/python3

import board
import neopixel

from subprocess import call

import threading
import time

from flask import Flask
from flask import render_template


# Flask setup
app = Flask(__name__)

# Hardware setup
pixels = neopixel.NeoPixel(board.D18, 43)
rooms = [0] * 43
lights = [0] * 43


# Setup the home page
@app.route('/')
def index():
    return render_template('index.html')


# Setup the room control
@app.route('/room<int:room_number>')
def handle_request(room_number):
    response = 'Room ' + str(room_number) + ' toggled'
    rooms[room_number - 1] = (( rooms[room_number - 1] + 1) % 2)
    
    # Turn the LEDs on and off
    for i in range(len(rooms)):
        pixels[i] = (50*rooms[i], 50*rooms[i], 50*rooms[i])
        
    return response, 200


# Draw the Path
def path():
    # Reset the rooms and LEDs when the path animation starts
    for i in range(len(rooms)):
        rooms[i] = 0
    pixels.fill((0, 0, 0))

    # Run the animation while no rooms are lit
    i = 3
    while not any(rooms):

        if ( i < 25 ):
            pixels[i] = (50, 0, 0)
        else:
            pixels[i] = (0, 0, 50)

        pixels[i-1] = (0, 0, 0)
        time.sleep(0.5)
        i += 1
        if ( i > 43 ): i = 3
    return


# Handle a path request
@app.route('/path')
def handle_path():
    # Start a thread to run the path
    pixels.fill((0, 0, 0))            
    path_thr = threading.Thread(target=path)
    path_thr.start()
    
    return 'User flow animation', 200


# Shutdown the Pi
@app.route('/shutdown')
def handle_shutdown():
    call("sudo nohup shutdown -h now", shell=True)
    return 'Shutting down Pi', 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
