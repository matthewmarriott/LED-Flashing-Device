from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
while True:
    led.toggle()
    sleep(3)
    
    	# FLASHING LIGHT PROJECT__________________________________________
	# This is a project to program a LED light - inserting a number after sleep( gives the seconds of the flash
	# on the microcontroller board, the Raspberry Pi Pico
    	# By Matthew Marriott 2022
    	# Uses Thonny with Micropython