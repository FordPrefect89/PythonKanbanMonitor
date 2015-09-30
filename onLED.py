#!/usr/bin/python

import RPi.GPIO as GPIO
import LPD8806

def ledOn():
    l = LPD8806.strand()
    l.set(0,100,0,0)
    l.set(1,0,100,0)
    l.set(2,0,0,100)
    l.set(3,100,100,0)
    l.set(4,0,100,100)
    l.set(5,100,0,100)
    l.set(6,100,100,100)
    l.fill(255,0,0,7,32)
    l.update()

ledOn()
