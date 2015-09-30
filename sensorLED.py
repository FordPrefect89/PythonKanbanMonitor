#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import LPD8806

def RangeDetect(trig, echo):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(trig, GPIO.LOW)
    GPIO.setup(echo,GPIO.IN)

    """ Sleep needed to avoid timing issues """
    time.sleep(0.3)

    """ Trigger range finding  """
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    """ Get return time  """
    while GPIO.input(echo) == 0:
        signaloff = time.time()

    while GPIO.input(echo) == 1:
        signalon = time.time()

    """ Convert return from sensor to cm  """
    distance = (signalon - signaloff) * 17000

    """ Clean GPIO  """
    GPIO.cleanup()

    """ Return measurement  """
    return distance

def RedLED(firstPixel, secondPixel):
    """  This fades the leds from red to green in 25 step increments   """
    led = LPD8806.strand()    
    count1 = 250
    count2 = 0
    while count1 != 0:
        """ Fade green off  """
        led.set(firstPixel, 0, count1, 0)
        led.set(secondPixel, 0, count1, 0)
        led.update()
        count1 -= 25
    while count2 != 250:
        """ Fade red on  """
        led.set(firstPixel, count2, 0, 0)
        led.set(secondPixel, count2, 0, 0)
        led.update()
        count2 += 25
    return

def GreenLED(firstPixel, secondPixel):
    """  This fades the leds from red to green in 25 step increments  """
    led = LPD8806.strand()   
    count1 = 250
    count2 = 0
    while count1 != 0:
        """ Fade red off  """
        led.set(firstPixel, count1, 0, 0)
        led.set(secondPixel, count1, 0, 0)
        led.update()
        count1 -= 25
    while count2 != 250:
        """ Fade green on  """
        led.set(firstPixel, 0, count2, 0)
        led.set(secondPixel, 0, count2, 0)
        led.update()
        count2 += 25
    return

def SlotStatus(rangeInfo):
    """  This determines if the slot is empty or full depending on the range  """
    if rangeInfo >= 3 and rangeInfo <= 10:
        """ Full Slot """
        status = 1
        return status
    else:
        """ Empty Slot """
        status = 0
        return status
    
def XMLWrite(one, two, three, four, five, six, seven, eight):
    """ This writes the XML file to the RAM drive.  Uses RAM drive to minimize
        hits on the SD card  """
    filePath = "/mnt/RAM/kanban.xml"
    xmlFile = open(filePath, 'w')

    xmlFile.write('<kanbanShelf>\n')
    xmlFile.write('     <one>%s</one>\n' % one)
    xmlFile.write('     <two>%s</two>\n' % two)
    xmlFile.write('     <three>%s</three>\n' % three)
    xmlFile.write('     <four>%s</four>\n' % four)
    xmlFile.write('     <five>%s</five>\n' % five)
    xmlFile.write('     <six>%s</six>\n' % six)
    xmlFile.write('     <seven>%s</seven>\n' % seven)
    xmlFile.write('     <eight>%s</eight>\n' % eight)
    xmlFile.write('</kanbanShelf>')

"""  To enable the constant looping  """
endRun = 1
"""  Used to know if the slot if full or empty  """
bGood = [1, 1, 1, 1, 1, 1, 1, 1]
"""  Used to determine if the green LED's are on or off  """
gOn = [1, 1, 1, 1, 1, 1, 1, 1]
"""  Used to determine if the red LED's are on or off  """
rOn = [0, 0, 0, 0, 0, 0, 0, 0]
sensor = [0, 0, 0, 0, 0, 0, 0, 0]
while endRun != 0:
    """Sensor pins.  ([TRIGGER], [ECHO])"""
    sensor[0] = round(RangeDetect(24, 25), 1)
    sensor[1] = round(RangeDetect(24, 25), 1)
    sensor[2] = round(RangeDetect(24, 25), 1)
    sensor[3] = round(RangeDetect(24, 25), 1)
    sensor[4] = round(RangeDetect(24, 25), 1)
    sensor[5] = round(RangeDetect(24, 25), 1)
    sensor[6] = round(RangeDetect(24, 25), 1)
    sensor[7] = round(RangeDetect(24, 25), 1)

    """  Gets the status of each sensor  (Now just doing it on one)  """
    slotOne = SlotStatus(sensor[0])
    slotTwo = SlotStatus(sensor[1])
    slotThree = SlotStatus(sensor[2])
    slotFour = SlotStatus(sensor[3])
    slotFive = SlotStatus(sensor[4])
    slotSix = SlotStatus(sensor[5])
    slotSeven = SlotStatus(sensor[6])
    slotEight = SlotStatus(sensor[7])

    """  Passes slot status to the XML file writing function  """
    XMLWrite(slotOne, slotTwo, slotThree, slotFour, slotFive, slotSix, slotSeven, slotEight)

    """ This is to check if LED is green or red  """
    """ Will need its own method for each LED segment  """
    """ This is only going to change LED's 1 and 2 """
    for count in range(0, 8):
        
        ledSet = 0
        if count == 0:
            ledSet = 0
        elif count == 1:
            ledSet = 2
        elif count == 2:
            ledSet = 4
        elif count == 3:
            ledSet = 6
        elif count == 4:
            ledSet = 8
        elif count == 5:
            ledSet = 10
        elif count == 6:
            ledSet = 12
        elif count == 7:
            ledSet = 14

        if sensor[count] >= 3 and sensor[count] <= 10:
            bGood[count] = 1
        else:
            bGood[count] = 0
        
        if bGood[count] == 1 and gOn == 0:
            GreenLED(ledSet, ledSet + 1)
            gOn[count] = 1
            rOn[count] = 0
            
        if bGood[count] == 0 and rOn == 0:
            RedLED(ledSet, ledSet + 1)
            gOn[count] = 0
            rOn[count] = 1
    """
    if sensor[0] >= 3 and sensor[0] <= 10:
        bGood[0] = 1
    else:
        bGood[0] = 0

    if bGood[0] == 1 and gOn[0] == 0:
        GreenLED(1, 2)
        gOn[0] = 1
        rOn[0] = 0

    if bGood[0] == 0 and rOn[0] == 0:
        RedLED(1, 2)
        gOn[0] = 0
        rOn[0] = 1
    """
    """ Sleep time to delay loop  """
    time.sleep(0.5)
