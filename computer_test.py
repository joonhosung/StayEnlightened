from computer_v1 import *

def main():
	# call the state function repeatedly
	state= False
	turnoff= True

	i=0
	while i<8:
		check_motion(state, turnoff)
		
		if i==3:
			turnoff=False
			print("Turning on camera outside")
			
		if i==5:
			turnoff=True
			print("Turning off camera outside")

		i+=1

main()	
				
	
