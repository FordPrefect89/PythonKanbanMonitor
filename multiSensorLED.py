#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import LPD8806
import ranging
import status
import flipLED
import FileOutput

slotState = status.CurrentStatus()
distance = ranging.range()
led = LPD8806.strand()
ledChange = flipLED.LEDFlip()
fileOps = FileOutput.FileWrite()

""" To enable the constant looping. Set to 0 (zero) for one iteration only. """
endRun = 1

""" Used to know if the slot if full or empty """
bGood = [1, 1, 1, 1, 1, 1, 1, 1]
""" Used to determine if the green LED's are on or off """
gOn = [1, 1, 1, 1, 1, 1, 1, 1]
""" Used to determine if the red LED's are on or off """
rOn = [0, 0, 0, 0, 0, 0, 0, 0]
""" Status of the slot array """
curStatus = [0, 0, 0, 0, 0, 0, 0, 0]
""" Slot range array """
slot = [0, 0, 0, 0, 0, 0, 0, 0]
""" Array of LED's for first pixel """
ledSel = [2, 3, 4, 6, 8, 10, 12]
cnt = 0

""" LEDChange flips the leds from one color to the other based on previous status  """
def LEDChange(arrayCnt, greenLED, redLED, goodCheck, startLED):
    if goodCheck[arrayCnt] == 1 and greenLED[arrayCnt] == 0:
        ledChange.GreenLED(led, startLED, startLED + 1)
        greenLED[arrayCnt] = 1
        redLED[arrayCnt] = 0

    if goodCheck[arrayCnt] == 0 and redLED[arrayCnt] == 0:
        ledChange.RedLED(led, startLED, startLED + 1)
        greenLED[arrayCnt] = 0
        redLED[arrayCnt] = 1

while endRun != 0:
    """ Sensor pins.  round(distance.RangeDetect([TRIGGER pin], [ECHO pin], value to round to))
        Trigger pin should always be the same to limit use of GPIO pins. """
    slot[0] = round(distance.RangeDetect(24, 25), 1)
    slot[1] = round(distance.RangeDetect(24, 25), 1)
    slot[2] = round(distance.RangeDetect(24, 25), 1)
    slot[3] = round(distance.RangeDetect(24, 25), 1)
    slot[4] = round(distance.RangeDetect(24, 25), 1)
    slot[5] = round(distance.RangeDetect(24, 25), 1)
    slot[6] = round(distance.RangeDetect(24, 25), 1)
    slot[7] = round(distance.RangeDetect(24, 25), 1)

    count = [0, 1, 2, 3, 4, 5, 6, 7]

    for cnt in count:
        curStatus[cnt] = slotState.SlotStatus(slot[cnt])
        
        if curStatus[cnt] == 1:
            bGood[cnt] = 1
        else:
            bGood[cnt] = 0

    """ LEDChange() flips the LED based on previous status  """
    """ The values to pass are as follows
        Sensor number (0 - 7)               arrayCnt
        Green and Red status arrays         greenLED, redLED
        Good check array                    goodCheck
        Starting LED number.                startLED
        Current setup only lights up 2 LED's per sensor input. """
    LEDChange(0, gOn, rOn, bGood, 0)
    LEDChange(1, gOn, rOn, bGood, 2)
    LEDChange(2, gOn, rOn, bGood, 4)
    LEDChange(3, gOn, rOn, bGood, 6)
    LEDChange(4, gOn, rOn, bGood, 8)
    LEDChange(5, gOn, rOn, bGood, 10)
    LEDChange(6, gOn, rOn, bGood, 12)
    LEDChange(7, gOn, rOn, bGood, 14)

    """Passes slot status to the XML file writing function"""
    fileOps.XMLWrite(curStatus[0], curStatus[1], curStatus[2], curStatus[3], curStatus[4], curStatus[5], curStatus[6], curStatus[7])
    
    """time.sleep(0.5)"""
