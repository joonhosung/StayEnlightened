## reads in data from Arduino
import serial
from time import sleep

# have to specify port name below
port='COM6'
ser = serial.Serial(port, 9600) # Establish the connection on a specific port
i=0
while i<10:
	
	msg=str(ser.readline().strip().decode('ascii')) # reads from Arduino
	print("message: "+msg)
	sleep(.1) # Delay for one tenth of a second
	if (msg=='0'):
		print("starting")
	elif (msg=='1'):
		print("turn on")
	else:
		print("turn off")
	i+=1
