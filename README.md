# Interactive Museum

A program to control WS2812b LEDs in a 1:200 scale model museum to demonstrate the user flow through the a museum.
It will also allow rooms to be individually lit from a web-app running locally on the Pi.

## User Flow
To demonstrate the user flow, LEDs will be stuck to the model in the same direction that users will walk through it. A simple function will illuminate the LEDs in sequencee and turn them off once the next is lit.

## Room control
A Pi will host a webpage with the four floorplans of the Museum, each room in the museum will be click-able and will light up and LED in the corresponding position of the phyical model. When pressing the room on the device, the image will update to demonstarte on the screen if a room is lit or not.

## Electronics
The LEDs will be a WS2812b strip controlled through a logic level shifter to the Pi.
A minimum of 60LEDs will be required to light the user flow as well as another 20LEDs to control the rooms. The use of LEDs for the user flow and room control and be shared as they are not functions that can be run simultaniously. Therefore, if all rooms are lit simultaniously in room mode, 20*50mA &rarr; 1A will be required. Assuming an absolute worst case, of no shared LEDs and all LEDs lit (a case which should not be possible), then 80*50mA &rarr 4A will be required.

The Raspberry Pi should be able to supply ~1.5A from its 5V GPIO pin, so could theoretically be used to run all the LEDs in the model under it's assumed conditions. However, given that a 4A charger covers the worst case, and will allow the LEDs to be used in future scenarios; it will be used.

The Pi will be powered with by one supply through it's USB micro-B port, although it could be powered through GPIO from the LEDs supply. The data-pin of the LEDs will be connected through a 330Ω resistor to a logic level shifter to the Pi. The ground through the Pi and to the 5V LED supply will be connected. The 5V supply will be connected to the V+ of the LEDs. There will be a 100uF capacitor connected across the 5V power supply.

## Display
* The electronics will be held in a plastic project enclosure box.
* The LEDs will be attached to the ceiling of each floor in the model.

## Usage
The Pi will be programmed to automatically start the webserver with the user flow function on boot. In order to change the behaviour, the user must connect to the Pi's AP and access the Pi's ip address on port 5000 in any webbrowser.

## Requirements
* Pi setup to run in [AP mode](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)
* 5V, 4A power supply
* Python3
* Pip3
* Pip modules &rarr; rpi_ws281x, adafruit-circuitpython-neopixel, flask


## ToDo
~~Python script sends the entire array~~ (removed arduino)
~~Arduino need to interpret the array and turn on the specfic LEDs~~ (removed arduino)
- [ ] Change IP address in JS  
- [x] Make pi run local server
- [ ] Change hostname of pi
- [ ] Room status is controlled independantly in Python script and JS &rarr; update this
