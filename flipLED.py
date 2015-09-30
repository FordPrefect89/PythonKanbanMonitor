#!/usr/bin/python

class LEDFlip:

    def RedLED(self, led, firstPixel, secondPixel):
        """ This fades the LED's from green to red in 25 step increments """
        count1 = 150
        count2 = 0
        while count1 != 0:
            led.set(firstPixel, count2, count1, 0)
            led.set(secondPixel, count2, count1, 0)
            led.update()
            count1 -= 25
            count2 += 25
        return
        
    def GreenLED(self, led, firstPixel, secondPixel):
        """ This fades the LED's from red to green in 25 step increments """
        count1 = 150
        count2 = 0
        while count1 != 0:
            led.set(firstPixel, count1, count2, 0)
            led.set(secondPixel, count1, count2, 0)
            led.update()
            count1 -= 25
            count2 += 25
        return
