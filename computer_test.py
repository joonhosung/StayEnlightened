from computer_v1 import *
from time import sleep
def main():
    # call the state function repeatedly
    state= False
    turnoff= True

    i=0
    while i<15:
        sleep(5)
        state=check_motion(state, turnoff)
        print("state: ", state)
        if state==True:
            print ("camera is on")
            turnoff=False

        if i==3:
            turnoff=True
            print("Turning off camera outside")

        i+=1

main()	
				
	
