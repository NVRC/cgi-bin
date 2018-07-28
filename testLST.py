from ledSerialTunnel import LedSerialTunnel

lct = LedSerialTunnel(int(255))

color = '00ff00'
count = 0
while count < 60:
    lct.addColor(color)
    count = count + 1
