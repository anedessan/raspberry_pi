#!/usr/bin/python3

import RPi.GPIO as GPIO #GPIO Kontrolle für Raspberry Pi einbinden
import time #Zur Zeitverzögerung
import random
GPIO.setmode(GPIO.BCM) #Ansprache der GPIOs über GPIO Nummer möglich

gpio_outputs = [23, 24, 25]
gpio_inputs = 12

def setup():
        for i in gpio_outputs:
           GPIO.setup(i, GPIO.OUT)
        GPIO.setup(gpio_inputs, GPIO.IN)

def alles_aus():
        for i in gpio_outputs:
                GPIO.output(gpio_outputs, GPIO.LOW)

#Start
setup()
GPIO.output(23, GPIO.HIGH)


status = ["rot", "rot-gelb", "gruen", "gelb"]
button = True



for i in status:
        if i == "rot":
            alles_aus()
            GPIO.output(23, GPIO.HIGH)
        if i == "rot-gelb":
                alles_aus()
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(24, GPIO.HIGH)
        if i == "gruen":
                alles_aus()
                GPIO.output(25, GPIO.HIGH)
        if i == "gelb":
                alles_aus()
                GPIO.output(24, GPIO.HIGH)
        time.sleep(2)






GPIO.cleanup() #Channel Belegung sauber machen