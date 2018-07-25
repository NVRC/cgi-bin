class LedSerialTunnel(object):

    def __init__(self, b):
        import serial
        self.brightness = b
        self.port = "/dev/ttyUSB0"
        self.colorArray = ""
        self.count = 0
        self.ser = serial.Serial(PORT,9600)
        self.ser.write(b'0')
        self.ser.write(b)

    def addColor(self, colorHex):
        self.colorArray += colorHex
        self.count = self.count + 1
        if count == 10:
            self.ser.write(self.colorArray)
            self.colorArray = ""
            self.count = 0
