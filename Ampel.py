#!/usr/bin/python3

import RPi.GPIO as GPIO #GPIO Kontrolle für Raspberry Pi einbinden
import time #Zur Zeitverzögerung
import random
GPIO.setmode(GPIO.BCM) #Ansprache der GPIOs über GPIO Nummer möglich

gpio_outputs = [23, 24, 25]

for i in gpio_outputs:
    GPIO.setup(i, GPIO.OUT)

t = 0 #ampeldurchlauf

GPIO.output(23, GPIO.HIGH)
for t in range(1):
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



#disco

t = 0

for i in gpio_outputs:
        GPIO.output(i, GPIO.LOW)

for t in range(100):
        r = random.randint(23,25)
        GPIO.output(r, GPIO.HIGH)
        time.sleep(0.1)
        for i in gpio_outputs:
                GPIO.output(i, GPIO.LOW)


GPIO.cleanup() #Channel Belegung sauber machen