import sys
import RPi.GPIO as GPIO

VALID_INPUTS = ['ON', 'OFF']

# Set this value to the GPIO pin used to toggle the power relay 
POWER_PIN = 17

# Display usage information
def print_help():
    print('Station Power Control')
    print('\nControl radio master power.  Power defaults to ON when RPi is offline.')
    print('\nUsage:')
    print('\n    "stationPower.py ON"  - Turn station power on')
    print('    "stationPower.py OFF" - Turn station power off')
    exit(0)

# If arguments are missing or invalid, display help and exit
if len(sys.argv) != 2 or sys.argv[1].upper() not in VALID_INPUTS:
    print_help()

# Disable GPIO warnings
GPIO.setwarnings(False)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_PIN, GPIO.OUT)

# Turn the IOT relay power ON or OFF
# Note that this is configured for a NORMALLY ON configuration, IE when the GPIO pin goes high the relay will turn off
if sys.argv[1].upper().strip() == 'ON':
    print('Turning on station power...')
    print('Finished.')
    GPIO.output(POWER_PIN, GPIO.LOW)

if sys.argv[1].upper().strip() == 'OFF':
    print('Turning off station power...')
    print('Finished.')
    GPIO.output(POWER_PIN, GPIO.HIGH)
