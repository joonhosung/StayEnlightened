# reads in data from Arduino
# have to specify port name below
import serial
from time import sleep

# State: stat of camera
port='/dev/tty96B0'
ser = serial.Serial(port, 9600) # Establish the connection on a specific port

def check_motion(state, turnOff):
	
	#port='COM6'
	# have to specify port name below
	
	if state==False:
		# inactive state
		# The computer will continuously read string from serial

		rsv=read_serial(ser)

		# if serial signals to start camera [1], return to external
		if rsv=='1':
			print("Motion detected! Turning on Camera.")
			state=True
			
	elif state==True:
		# inactive state
		# Computer stops reading from serial port
		# Continously writes to Arduino number of people
		
		# checks if turnOff==True
		if turnOff:
			# switch state to inactive
			state=False
			write_serial(ser)
			print("No humans... Turning camera off")
			
		

	# Return state, no matter if it changed or not.
	return state					




def read_serial(ser):
	msg=str(ser.readline().strip().decode('ascii')) # reads from Arduino and interpret as ascii
	print("message: "+msg)
	return msg

def write_serial(ser):
        # ser is the serial object; s is the data to be serially transmitted
	s = 'c'
	ser.write(s.encode()) # writes letter to Arduino
	
	return True


#main()
