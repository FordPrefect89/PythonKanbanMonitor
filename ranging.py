#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class range:

     def RangeDetect(self, trig, echo):
          GPIO.setwarnings(False)
          GPIO.setmode(GPIO.BCM)
          GPIO.setup(trig, GPIO.OUT)
          GPIO.setup(trig, GPIO.LOW)
          GPIO.setup(echo, GPIO.IN)
          
          time.sleep(0.3)
          
          GPIO.output(trig, True)
          time.sleep(0.00001)
          GPIO.output(trig, False)
          
          while GPIO.input(echo) == 0:
               signaloff= time.time()
          
          while GPIO.input(echo) == 1:
               signalon = time.time()
          
          distance = (signalon - signaloff) * 17000
          
          GPIO.cleanup()
          
          return distance
