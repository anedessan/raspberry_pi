#!usr/bin/python3

import RPi.GPIO as GPIO #GPIO Kontrolle für Raspberry Pi einbinden
import time #Zur Zeitverzögerung
GPIO.setmode(GPIO.BCM) #Ansprache der GPIOs über GPIO Nummer möglich

GPIO.setup(23, GPIO.OUT) #(GPIO23 kann als Output verwendet werden)

for i in range(5):
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)