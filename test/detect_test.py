#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Connect the Output pin from the sensor to the 7th Pin on the PiZeroW
iSensorPin = 7

# Set Pin Numeration to Board :  Top Row odd, Bottom Row even
# Set the selected Pin as input
GPIO.setmode(GPIO.BOARD)
GPIO.setup(iSensorPin, GPIO.IN)

def printTime():
	# Get the current time and format it to fit the output
	current_time = time.strftime("%Y-%m-%d %H:%M:%S")
	print("Movement detected: ", current_time)

def motionDetected(iSensorPin):
	printTime()
	time.sleep(5)

time.sleep(2)
print("Ready!")

try:
	# Add detection event for selected pin. If a Rising is detected, call function with bouncetime 1000
	GPIO.add_event_detect(iSensorPin, GPIO.RISING, callback=motionDetected, bouncetime=1000)
	while True:
		pass

except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()

