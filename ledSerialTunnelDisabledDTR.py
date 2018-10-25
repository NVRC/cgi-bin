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
        self._ser.open()
        time.sleep(0.1)
        self._ser.write('<0>'.encode('utf-8'))
        time.sleep(0.1)

        self._ser.write("<{:02x}>".format(self._brightness).encode('utf-8'))
        time.sleep(0.1)
    def addColor(self, colorHex):

        self._colorArray += colorHex
        self._count = self._count + 1
        if self._count == 60:
            self.writeColors()

    def writeColors(self):
        self._colorArray += ">"
        print("colorArray: ",end=self._colorArray,flush=True)
        self._ser.write(self._colorArray.encode('utf-8'))
        self._colorArray = "<"
        self._count = 0

    def isOpen(self):
        if self._ser.isOpen() == True:
            return True
        else:
            return False

    def setColorList(self, colorList):
        self._colorArray += colorList
        print("ColorList: ", end=colorList,flush=True)
        self.writeColors()


    def close(self):
        self._ser.close()
