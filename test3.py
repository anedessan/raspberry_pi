#!usr/bin/python3

import RPi.GPIO as GPIO #GPIO Kontrolle für Raspberry Pi einbinden
import time #Zur Zeitverzögerung
GPIO.setmode(GPIO.BCM) #Ansprache der GPIOs über GPIO Nummer möglich

gpio_in_list = 24
gpio_out_list = 23

GPIO.setup(gpio_out_list, GPIO.OUT) #(GPIO23 kann als Output verwendet werden)
GPIO.setup(gpio_in_list, GPIO.IN) #Am GPIO24 hängt der Schalter dran

for i in range(5):
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)


print("Jetzt Schalter drücken!")
time.sleep(2)

while True:
    if GPIO.input(24) == 0:
        GPIO.output(23, GPIO.LOW) #aus
    else:
        GPIO.output(23, GPIO.HIGH) #ein


GPIO.cleanup() #Channel Belegung sauber machen