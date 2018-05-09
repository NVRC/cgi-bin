#!/usr/bin/python
import cgi
import cgitb
from dotstar import Adafruit_DotStar
from led_drivers import nLevelLinearGradient as nllg
from led_drivers import gradientHelpers as gh
cgitb.enable()
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
	temp = gh.dotstarlibalt_correction(fs[str(key)].value)
	print(str(key)+' 0x%06x' % int(temp,16))
	strip.setPixelColor(i,int('0x%06x' % int(temp,16),16))
	i = i + 1
strip.setBrightness(int(fs["brightness"].value,10))
strip.show()
