void setup(){
	Serial.begin(9600);
	Serial.println(0);
}


void loop(){
	// transmits data to python

	Serial.println(1);
	char c=Serial.read();
	Serial.println(c);
}
