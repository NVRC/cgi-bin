#!/usr/bin/python
import cgi
import cgitb
import shelve
from dotstar import Adafruit_DotStar
from led_drivers import nLevelLinearGradient as nllg
from led_drivers import gradientHelpers as gh
db = 'color_shelf.db'
def addToShelf(index, color):
	s = shelve.open(db)
	try:
		s[str(index)] = color
	finally:
		s.close()


cgitb.enable()
fs = cgi.FieldStorage()


argString =""
nullCount = 0
close = False
for key in fs.keys():
	if str(fs[key].value) == "000000":
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
	if nullCount >= 60:
		s = shelve.open(db)
		try:
			temp = s[str(i)]
			if i == 59:
				close = True
			else:
				pass
		finally:
			if close:
				s.close()
	else:
		temp = gh.dotstarlib_correction(fs[str(key)].value)
		print(str(key)+' 0x%06x' % int(temp,16))
		temp = int('0x%06x' % int(temp,16),16)
		addToShelf(i,temp)
	strip.setPixelColor(i,temp)
	i = i + 1
strip.setBrightness(int(fs["brightness"].value,10))
strip.show()
