#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def RangeDetect(trig, echo):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(trig, GPIO.LOW)
    GPIO.setup(echo,GPIO.IN)

    time.sleep(0.3)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        signaloff = time.time()

    while GPIO.input(echo) == 1:
        signalon = time.time()

    distance = (signalon - signaloff) * 17000

    GPIO.cleanup()

    return distance

def SlotStatus(rangeInfo):
    if rangeInfo >= 3 and rangeInfo <= 10:
        """ Full Slot """
        status = 1
        return status
    else:
        """ Empty Slot """
        status = 0
        return status
    

endRun = 1
while endRun != 0:
    filePath = "/mnt/RAM/kanban.xml"
    '''sensorOne = round(RangeDetect(17, 27), 1)'''
    sensorTwo = round(RangeDetect(17, 22), 1)

    '''slotOne = SlotStatus(sensorOne)'''
    slotTwo = SlotStatus(sensorTwo)

    xmlFile = open(filePath, 'w')
    xmlFile.write('<kanbanShelf>\n')
    '''xmlFile.write('     <one>%s</one>\n' % slotOne)'''
    xmlFile.write('     <two>%s</two>\n' % slotTwo)
    xmlFile.write('</kanbanShelf>\n')
    xmlFile.close()

    print "Sensor read done"
    print " "
    time.sleep(2.5)

    endRun = endRun - 1

    """
    if sensorOne >= 3 and sensorOne <= 10:
        print "Slot 1 Full", sensorOne
    else:
        print"Slot 1 Empty", sensorOne

    if sensorTwo >= 3 and sensorTwo <= 10:
        print "Slot 2 Full", sensorTwo
    else:
        print "Slot 2 Empty", sensorTwo

    time.sleep(2.5)

    
    print "Sensor 1 reading:", round(RangeDetect(17, 27), 1),"cm"
    print "Sensor 2 reading:", round(RangeDetect(17, 22), 1),"cm"
    print " "
    """
