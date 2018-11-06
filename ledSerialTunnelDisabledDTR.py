class LedSerialTunnelDisabledDTR(object):

    def __init__(self, b):
        import serial
        import struct
        import time
        self._brightness = int(float(b))
        self._port = "/dev/ttyUSB0"
        self._colorArray = "<"
        self._count = 0
        self._ser = serial.Serial()
        self._ser.port = self._port
        self._ser.baudrate = 9600
        self._rate = 0
        self._cmd = 0;
        self._ser.open()
        time.sleep(0.1)






    def addColor(self, colorHex):
        self._colorArray += colorHex
        self._count = self._count + 1
        if self._count == 60:
            self.writeColors()

    def writeColors(self):
        import time

        if self._rate != 0:
            self._ser.write('<{:01x}>'.format(self._cmd).encode('utf-8'))
            time.sleep(0.1)
        else:
            self._ser.write('<0>'.encode('utf-8'))
            time.sleep(0.1)

        if self._rate != 0:
            self._ser.write('<{:03x}>'.format(self._rate).encode('utf-8'))
            time.sleep(0.1)

        self._ser.write('<{:02x}>'.format(self._brightness).encode('utf-8'))
        time.sleep(0.1)


        self._colorArray += ">"
        self._ser.write(self._colorArray.encode('utf-8'))
        self._colorArray = "<"
        self._count = 0

    def setRate(self, rate):
        self._rate = rate

    def setCmd(self, cmd):
        self._cmd = cmd

    def isOpen(self):
        if self._ser.isOpen() == True:
            return True
        else:
            return False

    def setColorList(self, colorList):
        self._colorArray += colorList
        self.writeColors()


    def close(self):
        self._ser.close()
