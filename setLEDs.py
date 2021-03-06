#!/usr/bin/python3
import cgi
import cgitb
import shelve
import sys
from ledSerialTunnelDisabledDTR import LedSerialTunnelDisabledDTR

db = 'color_shelf.db'
def addToShelf(index, color):
	s = shelve.open('color_shelf')
	try:
		s[str(index)] = color
	finally:
		s.close()

argFlag = False
brightness = 1000
webFlag = False
if len(sys.argv) > 1:
	argFlag = True
	if sys.argv[1] == 'on':

		brightness = 255
	elif sys.argv[1] == 'off':

		brightness = 0
	else:
		webFlag = True


if webFlag == True:
	cgitb.enable()
	fs = cgi.FieldStorage()
	brightness = int(fs["brightness"].value,10)


argString =""
nullCount = 0
close = False
if argFlag == False:
	for key in fs.keys():
		if str(fs[key].value) == "000000":
			nullCount = nullCount + 1

		argString +=fs[key].value
		argString += " "
	argString += fs["brightness"].value
	print("Content-Type: text/plain\n")
	print(argString)
#nllg.led_output(argString)
if brightness == 1000:
	brightness = int(fs["brightness"].value,10)
ldt = LedSerialTunnelDisabledDTR(brightness)

i = 0
for key in range(0,60):
	if nullCount >= 60 or argFlag == True:
		s = shelve.open('color_shelf')
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
		temp = fs[str(key)].value
		addToShelf(i,temp)
	ldt.addColor(temp)
	i = i + 1
