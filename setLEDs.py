#!/usr/bin/python
import cgi
import cgitb
import shelve
from dotstar import Adafruit_DotStar
from led_drivers import nLevelLinearGradient as nllg
from led_drivers import gradientHelpers as gh
cgitb.enable()
fs = cgi.FieldStorage()
db = 'color_shelf.db'

argString =""
nullCount = 0
for key in fs.keys():
	if(fs[key].value == "ffffff"):
		nullCount = nullCount + 1

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
	if(nullCount >= 60):
		s = shelve.open(db)
		try:
			temp = s[str(i)]
			if (i = 59):
				close = True
	else:
		temp = gh.dotstarlibalt_correction(fs[str(key)].value)
		print(str(key)+' 0x%06x' % int(temp,16))
		temp = int('0x%06x' % int(temp,16),16)
		addToShelf(i,temp)
	strip.setPixelColor(i,temp)
	i = i + 1
	if (close):
		s.close()
strip.setBrightness(int(fs["brightness"].value,10))
strip.show()

def addToShelf(index, color):
	s = shelve.open(db)
	try:
		s[str(index)] = color
	finally:
		s.close()
