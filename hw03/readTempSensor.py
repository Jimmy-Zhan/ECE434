#!/usr/bin/env python3
# Read a TMP101 sensor

import smbus
import time

bus = smbus.SMBus(2)
address = 0x48
address2 = 0x49
while True:
	temp = bus.read_byte_data(address,0)
	temp2 = bus.read_byte_data(address2,0) 
	print("temp1: "+str(temp)+" temp2: " + str(temp2)  ,end="\r")
	
	time.sleep(0.25)
