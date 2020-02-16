# reads in data from Arduino
# have to specify port name below
import serial
from time import sleep


def main():
	#port='/dev/tty96B0'
	port='COM6'
	# have to specify port name below
	ser = serial.Serial(port, 9600) # Establish the connection on a specific port
	for i in range (0, 1000, 1):
		read_serial(ser)
		sleep(1)
		write_serial(ser, 'c')
		sleep(.1) # Delay for one tenth of a second


def read_serial(ser):
	msg=str(ser.readline().strip().decode('ascii')) # reads from Arduino and interpret as ascii
	print("message: "+msg)
	if (msg=='0'):
		print("No motion detected. Turning off camera.")
	elif (msg=='1'):
		print("Detected motion. Turning on camera.")
	else:
		print("No update from camera.")

	return True

def write_serial(ser, s):
        # passes in char
	ser.write(s.encode()) # writes letter to Arduino
	return True


main()
