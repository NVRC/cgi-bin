#!/usr/bin/python
import cgi
from dotstar import Adafruit_DotStar
from led_drivers import nLevelLinearGradient as nllg
fs = cgi.FieldStorage()
argString =""
for key in fs.keys():
	argString +=fs[key].value
	argString += " "
argString += fs["brightness"].value
print "Content-Type: text/plain\n"
print(argString)
#nllg.led_output(argString)
strip = Adafruit_DotStar(60)
strip.begin()
i = 0
for key in range(0,60):
	print(str(key)+' 0x%04x' % int(fs[str(key)].value,16))
	strip.setPixelColor(i,int('0x%04x' % int(fs[str(key)].value,16),16))
	i = i + 1
strip.setBrightness(int(fs["brightness"].value,10))
strip.show()
