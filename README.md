# Interactive Museum

A program to control WS2812b LEDs in a 1:200 scale model museum to demonstrate the visitor flow through the a museum. It will also allow rooms to be individually lit from a web-app running locally on a Raspberry Pi. In order to achieve the visitor flow animation, multi-threading will be required to allow the animation to run in the background.

<center>

| | |
|:---:|:---:|
| <img width="1604" alt="Demo Gif" src="https://github.com/PolygonHJ/interactive_museum/raw/master/assets/demo.gif">  Demo Video | <img width="1604" alt="Lit Rooms" src="https://github.com/PolygonHJ/interactive_museum/raw/master/assets/lit_rooms.png">  Rooms Lit |
| <img width="1604" alt="Underside of Ceiling" src="https://github.com/PolygonHJ/interactive_museum/raw/master/assets/below.png">  Underside of Ceiling | <img width="1604" alt="Side View" src="https://github.com/PolygonHJ/interactive_museum/raw/master/assets/section.png">  Side View |



![Underside of ceilings](https://github.com/PolygonHJ/interactive_museum/raw/master/assets/below.png "Underside")

![Side view](https://github.com/PolygonHJ/interactive_museum/raw/master/assets/section.png "Side View")

</center>


## Visitor Flow
To demonstrate the visitor flow, LEDs are stuck to the model and lit in an order to match the visitors journey. A simple function illuminates the LEDs in sequence and turns off the previous once the next is lit, at the halfway point the LEDs change colour to show that the visitor is now be going down floors.

## Room control
A Pi hosts a webpage with the floorplan of the Museum, each room in the museum is click-able and lights up and LED in the corresponding position of the phyical model. When pressing the room on the device, the element on the webpage updates to demonstarte on the screen if a room is lit or not.

## Electronics
The LEDs are an WS2812b strip controlled through a logic level shifter to the Pi. To address the rooms and run the animation, forty-three LEDs are required. The use of LEDs for the visitor flow and room control are shared where possible as they are not required simultaneously. Therefore, if all rooms are lit at one instance in room mode, 20*50mA &rarr; 1A will be required. The final model ended up using forty-two LEDs as one LED died and there was not another available to replace it.

The Raspberry Pi [should be able to supply ~1.5A](https://pinout.xyz/pinout/pin2_5v_power) from its 5V GPIO pin, so could theoretically be used to run all the LEDs in the model under it's programmed worst case condition (all rooms lit white &rarr; 1A). Under the worst case conidtion of a fault, in which all LEDs are set to be lit white, 2.15A will be required; a seperate charger should be considered but due to the immediate requirement of the project, the strip will be powered directly by the Pi.

The Pi is powered with by one supply through it's USB micro-B port, although it could be powered through GPIO along with the LED strip. The data-pin of the LEDs should be connected through a 330Ω resistor to a logic level shifter to the Pi. If using a separate supply for the LEDs the ground of the Pi and to the 5V supply should be connected. The 5V supply should be connected to the V+ of the LEDs. There will be a 100uF capacitor connected across the 5V power supply.

## Display
* The electronics are held in a plastic project enclosure box.
* The LEDs attached to the ceiling of each floor in the model.


## Code Outline
On boot, the python script runs the webserver (set in rc.local). The index page shows the floor-plans, each floor-plan is a css grid and rooms are overlayed onto the image of the floor-plan with a div represeting the rough room positioning. Selecting a div sends a URL request with the respective room to the server and alters the css to demonstrate the selected rooms state. The selection of any room in the floor-plan ends the visitor flow animation.

In order to allow the animation to run while the webserver is running, a multi-thread process has been setup.


## Usage
The Pi is programmed to automatically start the webserver on boot. In order to control the LEDs, the user must connect to the Pi's AP and access the Pi's ip address <http://192.168.0.10> on port 5000 in any web-browser.

## Requirements
* Pi setup to run in [AP mode](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)
* 5V, 2.5A power supply
* Python3
* Pip3
* Pip modules &rarr; rpi_ws281x, adafruit-circuitpython-neopixel, flask


## ToDo
- [x] Run on boot (rc.local)
- [x] Update room numbers
- [x] Add shutdown button
- [x] Change IP address in JS  
- [x] Make pi run local server  
- [x] Change colour of LEDs going up vs going down
- [x] Update UI with path animation button
- [ ] Improve threading
- [ ] Only run visitor flow animation once

~~- [ ] Change hostname of pi~~

~~- [ ] Room status is controlled independantly in Python script and JS &rarr; update this~~

~~Python script sends the entire array~~ (removed arduino)

~~Arduino need to interpret the array and turn on the specfic LEDs~~ (removed arduino)    