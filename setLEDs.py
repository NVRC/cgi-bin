#!/usr/bin/python3
import cgi
import cgitb
import shelve
import sys
from ledSerialTunnel import LedSerialTunnel

db = 'color_shelf.db'
def addToShelf(index, color):
	s = shelve.open('color_shelf')
	try:
		s[str(index)] = color
	finally:
		s.close()


cgitb.enable()
fs = cgi.FieldStorage()
argFlag = False
if len(sys.argv) > 1:
	if sys.argv[1] == 'on':
		argFlag = True
		brightness = 255
	elif sys.argv[1] == 'off':
		argFlag = True
		brightness = 0
else:
	brightness = int(fs["brightness"].value,10)

ldt = LedSerialTunnel(brightness)
argString =""
nullCount = 0
close = False
for key in fs.keys():
	if str(fs[key].value) == "000000":
		nullCount = nullCount + 1

	argString +=fs[key].value
	argString += " "
argString += fs["brightness"].value
print("Content-Type: text/plain\n")
print(argString)
#nllg.led_output(argString)


i = 0
for key in range(0,60):
	if nullCount >= 60 or argFlag == True:
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
		temp = fs[str(key)].value
		addToShelf(i,temp)
	ldt.addColor(temp)
	i = i + 1
