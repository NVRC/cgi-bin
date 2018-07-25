class LedSerialTunnel(object):

    def __init__(self, b):
        import serial
        self._brightness = b
        self._port = "/dev/ttyUSB0"
        self._colorArray = ""
        self._count = 0
        self._ser = serial.Serial(self._port,9600)
        self._ser.write(b'0')
        import time
        time.sleep(1)
        self._ser.write("0x{:02x}".format(self._brightness))

    def addColor(self, colorHex):
        self._colorArray += colorHex
        self._count = self._count + 1
        if self._count == 10:
            print("Adding a segment")
            print(self._colorArray)
            print(bytearray(self._colorArray))
            self._ser.write(bytearray(self._colorArray))
            self._colorArray = ""
            self._count = 0
            import time
            time.sleep(1)
