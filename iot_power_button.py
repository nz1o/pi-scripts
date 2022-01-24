'''
This script can be used to control the power of an IOT relay (such as this one https://www.amazon.com/Iot-Relay-Enclosed-High-Power-Raspberry/dp/B00WV7GMA2)
through the use of a momentary push button attached to a GPIO pin on the Raspberry Pi.  The momentary push button should be connected between any GPIO pin 
(pin 22 in this example) and GND.

In this example, shack power is connected to the NORMALLY ON side of the relay.  This means that the shack power will turn OFF when the GPIO pin is HIGH.
'''

from time import sleep
import RPi.GPIO as GPIO

# Set GPIO pin numbers for the momentary push button and IOT relay
POWER_PIN = 17
BUTTON_PIN = 22

# Disable GPIO warnings
GPIO.setwarnings(False) 

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_PIN, GPIO.OUT) 
GPIO.setup(BUTTON_PIN, GPIO.IN) 

# Loop continuously
while True:
    # If the GPIO pin goes LOW (button is pressed)
    if not GPIO.input(22):
        # If the power is ON (GPIO LOW), turn the power OFF (GPIO HIGH)
        if not GPIO.input(17):
            GPIO.output(17, GPIO.HIGH)
            sleep(2)
        else:            
            # If the power is OFF (GPIO HIGH), turn the power ON (GPIO LOW)
            GPIO.output(17, GPIO.LOW)
            sleep(2)
