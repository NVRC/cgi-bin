class LedSerialTunnel(object):

    def __init__(self, b):
        import serial
        import struct
        import time
        self._brightness = b
        self._port = "/dev/ttyUSB0"
        self._colorArray = "<"
        self._count = 0
        self._ser = serial.Serial()
        self._ser.port = self._port
        self._ser.baudrate = 9600
        #self._ser.timeout = 1
        #self._ser.setDTR(False)
        #self._ser.setRTS(False)
        self._ser.open()

        self._ser.write('<0>'.encode('utf-8'))

        self._ser.write("<{:02x}>".format(self._brightness).encode('utf-8'))
    def addColor(self, colorHex):
        import time
        self._colorArray += colorHex
        self._count = self._count + 1
        if self._count == 60:
            self._colorArray += ">"
            self._ser.write(self._colorArray.encode('utf-8'))
            self._colorArray = "<"
            self._count = 0


    def close(self):
        self._ser.close()
