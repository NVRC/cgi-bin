class LedSerialTunnel(object):

    def __init__(self, b):
        import serial
        self._brightness = b
        self._port = "/dev/ttyUSB0"
        self._colorArray = ""
        self._count = 0
        self._ser = serial.Serial()
        self._ser.port = self._port
        self._ser.baudrate = 9600
        self._ser.timeout = 1
        self._ser.open()
        #self._ser.setDTR(False)
        #self._ser.setRTS(False)

        self._ser.write(b'0')
        import time
        time.sleep(1)
        self._ser.write(chr(self._brightness))

    def addColor(self, colorHex):
        self._colorArray += colorHex
        self._count = self._count + 1
        if self._count == 10:
            print("Adding a segment")
            print(len(self._colorArray))
            print(len(str(self._colorArray)))
            self._ser.write(str(self._colorArray))
            self._colorArray = ""
            self._count = 0
            import time
            time.sleep(1)

    def close(self):
        self._ser.close()
