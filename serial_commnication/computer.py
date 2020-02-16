## reads in data from Arduino
import serial
from time import sleep
ser = serial.Serial('/dev/tty96B0', 9600) # Establish the connection on a specific port
i=0
while i<1000:
	
	msg=str(ser.readline().strip().decode('ascii')) # reads from Arduino
	print("message: "+msg)
	sleep(.1) # Delay for one tenth of a second
	if (msg=='0'):
		print("No motion detected. Turning off camera.")
	elif (msg=='1'):
		print("Detected motion. Turning on camera.")
	else:
		print("No update from camera.")
	i+=1
