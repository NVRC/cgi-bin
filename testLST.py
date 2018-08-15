from ledSerialTunnelDisabledDTR import LedSerialTunnelDisabledDTR

lct = LedSerialTunnelDisabledDTR(int(255))

color = '0000ff'
count = 0
while count < 60:
    lct.addColor(color)
    count = count + 1
lct.close()
