// Control WS2812b LEDs based on serial input
#include <FastLED.h>

// LED wiring
#define LED_PIN 	5
#define Num_LED 	30
#define LED_TYPE	WS2812
#define COLOR_ORDER	GRB
CRGB leds[NUM_LED]

// Room pins
const int room1[1] 	= {0};
const int room2[1] 	= {1};
const int room3[1] 	= {2};
const int room4[1] 	= {3};
const int room5[1] 	= {4};
const int room6[1] 	= {5};
const int room7[1] 	= {6};
const int room8[1] 	= {7};
const int room9[1] 	= {8};
const int room10[1] 	= {9};
const int room11[1] 	= {10};
const int room12[1] 	= {11};
const int room13[1] 	= {12};
const int room14[1] 	= {13};
const int room15[1] 	= {14};



int lit_rooms[] = {};

// Send the entire array to arduino?
int inArr(int arr, int room) {
	int i;
	for ( i = 0; i < sizeof(arr); i++ ) {
		// if element in array then remove?
		// get index and remove by index
	}
}

void setup() {
	serial.begin(9600);
	FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LED);
}

void loop() {
	
	if ( serial.available() > 0 ) {
		room = Serial.read();
		room = room.toInt();

		if ( 

