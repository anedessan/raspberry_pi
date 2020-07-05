#!/usr/bin/python3

import RPi.GPIO as GPIO #GPIO Kontrolle für Raspberry Pi einbinden
import time #Zur Zeitverzögerung
GPIO.setmode(GPIO.BCM) #Ansprache der GPIOs über GPIO Nummer möglich

gpio_outputs = [23, 24, 25]

for i in gpio_outputs:
    GPIO.setup(i, GPIO.OUT)

t = 0 #ampeldurchlauf

GPIO.output(23, GPIO.HIGH)
for t in range(5):
        #Step 1: Rot
        GPIO.output(23, GPIO.HIGH)
        time.sleep(3)

        #Step 2: Rot-Gelb
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)

        #Step3: Grün
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
        time.sleep(3)

        #Step4: Gelb
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)

        #Step5: wieder rot
        GPIO.output(24, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)




GPIO.cleanup() #Channel Belegung sauber machen