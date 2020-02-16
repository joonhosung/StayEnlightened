int state=1; // reports state of motion sensor 1 if active, 0 if inactive


void setup(){
	Serial.begin(9600);
	Serial.println(0);
}

void loop(){
	if (state==1){
		// active state

		// continuously reads in motion sensor value
		motion=readsensor() /*<---------------fix this with proper pin numbers and syntax--*/
		if (motion==1){
			// if motion sensor reports motion detected
			Serial.println(1); // prints a 1 to serial monitor and writes to python
			
			//switch state	
			state=0;
		}

	}

	else{
		// inactive state: reads in python value of number of people until no one, then turn off lights
		
		int num=Serial.read(); /*<----------------------fix with proper pin numbers and syntax--*/
		if (num==0){
			// no person detected in the frame
			
			// switch state
			state=1
			digitalWrite(); // turn off lights <---------------------turn off LED here
			
		}
	}


}
