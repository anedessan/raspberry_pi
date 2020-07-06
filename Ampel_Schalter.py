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


#Start
setup()
GPIO.output(23, GPIO.HIGH)


status = ("rot", "rot-gelb", "gruen", "gelb")








GPIO.cleanup() #Channel Belegung sauber machen