#!/usr/bin/python3

import serial
from flask import Flask
from flask import render_template

app = Flask(__name__)

lit_rooms = []
rooms = [[0],
        [1],
        [2]]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/room<int:room_number>', methods=["GET"])
def handle_request(room_number):
    # Room state is controlled independantly in javascript and python
    response = 'Room ' + str(room_number) + ' toggled'
    print(response)

    # Create room array
    ## Assuming only one led per room
    if ( rooms[room_number-1][0] in lit_rooms ):
        lit_rooms.remove(rooms[room_number-1][0])
    else:
        lit_rooms.append(rooms[room_number-1][0])

    # Set serial device
    ser = serial.Serial('dev/ttyUSB0')
    print(ser.name)
    ser.write(lit_rooms)
    ser.close()

    return response, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
