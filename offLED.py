#!/usr/bin/python

import RPi.GPIO as GPIO
import LPD8806

def ledOff():
    led = LPD8806.strand()
    led.fill(0,0,0)
    led.update()
    return

ledOff()
