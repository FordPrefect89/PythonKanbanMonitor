#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def reading(sensor):
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(24, GPIO.LOW)
    GPIO.setup(25,GPIO.IN)

    if sensor == 0:

        time.sleep(0.3)

        GPIO.output(24, True)
        time.sleep(0.00001)

        GPIO.output(24, False)

        while GPIO.input(25) == 0:
            signaloff = time.time()

        while GPIO.input(25) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff

        distance = timepassed * 17000

        return distance

        GPIO.cleanup()

endRun = 100
while endRun != 99:
    print "Sensor 1 reading:", round(reading(0), 1), "cm"
