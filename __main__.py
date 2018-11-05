#!/usr/bin/python3
import sys
from ledSerialTunnelDisabledDTR import LedSerialTunnelDisabledDTR

if len(sys.argv) == 3:
    ldt = LedSerialTunnelDisabledDTR(sys.argv[2])
    ldt.setColorList(sys.argv[1])
elif len(sys.argv) == 5:
    ldt = LedSerialTunnelDisabledDTR(sys.argv[2])
    ldt.setCmd(sys.argv[3])
    ldt.setRate(sys.argv[4])
    ldt.setColorList(sys.argv[1])
