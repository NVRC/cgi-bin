class LedSerialTunnel(object):

    def __init__(self, b):
        import serial
        self._brightness = b
        self._port = "/dev/ttyUSB0"
        self._colorArray = ""
        self._count = 0
        self._ser = serial.Serial(self.port,9600)
        self._ser.write(b'0')
        self._ser.write(b)

    def addColor(self, colorHex):
        self._colorArray += colorHex
        self._count = self._count + 1
        if self._count == 10:
            self._ser.write(self._colorArray)
            self._colorArray = ""
            self._count = 0
