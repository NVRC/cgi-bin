#!/usr/bin/python3
import sys
from ledSerialTunnelDisabledDTR import LedSerialTunnelDisabledDTR

ldt = LedSerialTunnelDisabledDTR(sys.argv[2])
ldt.setColorList(sys.argv[1])
