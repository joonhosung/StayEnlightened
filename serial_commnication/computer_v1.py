# reads in data from Arduino
# have to specify port name below
import serial
from time import sleep


def main():
	port='/dev/tty96B0'
	#port='COM6'
	# have to specify port name below
	ser = serial.Serial(port, 9600) # Establish the connection on a specific port

	active=False
	camera_on=False

	while state==False:
		# inactive state
		# The computer will continuously read string from serial

		rsv=read_serial(ser)

		# if serial signals to start camera [1], return to external
		if rsv=='1':
			state=True
			camera_on=True
			## take images?

	num=5
	while state==True:
		# inactive state
		# Computer stops reading from serial port
		# Continously writes to Arduino number of people
		
		# checks if number of people==0
		if num==0:
			# switch state to inactive
			state=False
			camera_on=False
			
			
		write_serial(ser, num)
		num-=1 #decrement by 1 here just for testing
						




def read_serial(ser):
	msg=str(ser.readline().strip().decode('ascii')) # reads from Arduino and interpret as ascii
	print("message: "+msg)
	return msg

def write_serial(ser, s):
        # ser is the serial object; s is the data to be serially transmitted
	ser.write(s.encode()) # writes letter to Arduino
	return True


main()
