from ledSerialTunnel import LedSerialTunnel

lct = LedSerialTunnel(int(254))

color = 'fd5659'
count = 0
while count < 60:
    lct.addColor(color)
    count = count + 1
