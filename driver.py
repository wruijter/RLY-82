import serial
from serial import Serial
import sys

# Python driver for USB-RLY82 board
# Based on documentation from https://robot-electronics.co.uk/files/usb-rly82.pdf

port = "/dev/ttyACM0"
ser = serial.Serial(port,baudrate=19200,timeout=5.0,write_timeout=5.0,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_TWO,bytesize=serial.EIGHTBITS)

def communicate(input):
  if input == "connection":
    print ser
  
  elif input == "serial": 
    ser.write(str("38").decode('hex')+'\r\n')
    out = ser.read(8)
    print out

  elif input == "version":
    ser.write(str("5a").decode('hex')+'\r\n')
    out = ser.read(2)
    print out.encode('hex')

  elif input == "gpio_state": 
    ser.write(str("5E").decode('hex')+'\r\n')
    out = ser.read(1)
    print out.encode('hex')

  elif input == "adcRef_show": 
    ser.write(str("80").decode('hex')+'\r\n')
    out = ser.read(8)
    print out.encode('hex')

  elif input == "adcRef_getAll": 
    ser.write(str("82").decode('hex')+'\r\n')
    out = ser.read(16)
    print out.encode('hex')

  elif input == "adcRef_setAll_4v": 
	ser.write(str("81"+"0"+"1").decode('hex')+'\r\n')
	out = ser.read(1)
	print out.encode('hex')

  elif input == "adcRef_setAll_2v": 
	ser.write(str("81"+"0"+"2").decode('hex')+'\r\n')
	out = ser.read(1)
	print out.encode('hex')

  elif input == "adcRef_setAll_USB": 
	ser.write(str("81"+"0"+"0").decode('hex')+'\r\n')
	out = ser.read(1)
	print out.encode('hex')

  elif input == "relay_state": 
      ser.write(str("5B").decode('hex')+'\r\n')
      out = ser.read(1)
      
      if(out.encode('hex')=="00"):
        print "left off, right off"
        
      elif(out.encode('hex')=="01"):
        print "left on, right off"
       
      elif(out.encode('hex')=="02"):
        print "left off, right on"   
        
      elif(out.encode('hex')=="03"):
        print "left on, right on"
             
  elif input == "relay_1_on":
    ser.write(str("65").decode('hex')+'\r\n')
    print "relay 1 turned on"
    
  elif input == "relay_2_on":
    ser.write(str("66").decode('hex')+'\r\n')
    print "relay 2 turned on"
    
  elif input == "relay_1_off":
    ser.write(str("6f").decode('hex')+'\r\n')
    print "relay 1 turned off"
    
  elif input == "relay_2_off":
    ser.write(str("70").decode('hex')+'\r\n')
    print "relay 2 turned off"
    

if len(sys.argv) == 1:
  while True:
    input = raw_input("command>> ")
    communicate(input)

elif len(sys.argv) == 2:
    communicate(sys.argv[1])

