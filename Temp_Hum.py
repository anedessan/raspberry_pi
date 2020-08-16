import Adafruit_DHT
import datetime
import os.path
from os import path

datum ="01.01.1970"
uhrzeit="00:00:00"
LOGPATH = "/Temperatur_Log"
LOGFILE = "temperatur.csv"
pfad = LOGPATH +'/'+LOGFILE
sensor = Adafruit_DHT.DHT22
pin = 4
csv_header = "Datum;Uhrzeit;Temperatur;Feuchtigkeit\n"
debug = True



def Zeit_auslesen():
    Time_Obj = datetime.now()
    datum = str(Time_Obj.day +"." + Time_Obj.month + "." + Time_Obj.year)
    uhrzeit = str(Time_Obj.hour + ":" + Time_Obj.minute +":" + Time_Obj.second)


humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

exisiting = path.exists(pfad)
file = open(pfad, "a")
if not exisiting:
    file.write(csv_header)
file.write(datum+';'+uhrzeit+';'+temperature+';'+humidity+'\n')
file.close()




#print('Temperatur: {0:0.1f}*C Luftfeuchtigkeit: {1:0.1f}%'.format(temperature,humidity))
