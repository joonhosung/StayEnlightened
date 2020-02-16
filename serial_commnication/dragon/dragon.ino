//This code will allow the PIR motion sensor to send updates to:
// 1. Turn on the camera if motion/people are detected
// 2. Turn off the camera if no motion is detected.

int pirState=1; // reports state of motion sensor: 1 if active, 0 if inactive

int lightPin = 11; //The "lights" to be controlled
int motionPin = 13; //Diagnostic Output pin - if motion detected
int inputPin = 2; //Input pin - the PIR sensor
int movement = 0; //Pin status (HIGH or LOW)


void setup(){
  pinMode(motionPin, OUTPUT); 
  pinMode(lightPin, OUTPUT);
  pinMode(inputPin, INPUT);
  Serial.begin(9600);
  Serial.println(0); //Do we want this here??
}

void loop(){
  if (pirState==1){
    // active state
 
    // continuously reads in motion sensor value
    movement = digitalRead(inputPin); //Read PIR input

    //If motion sensor reports motion detected
    if (movement == HIGH){ 
      digitalWrite(lightPin, HIGH); //Turn on the lights.
      digitalWrite(motionPin, HIGH); //Diagnostic pin - HIGH if PIR triggered.
      Serial.println(1); // prints a 1 to serial monitor and writes to python
      //Send serial data to python -> computer_v1.py, which will tell the camera to turn on and take pictures in OpenCV
      //switch state	
      pirState=0; 
      
    } else { //No movement
        digitalWrite(motionPin, LOW); //Turn diagnostic output off.
        Serial.println(0);
    }
  
  } else {
    // inactive state: reads in python value of number of people until no one, then turn off lights
    delay(100);
    Serial.println(0); //Ensure that arduino does not write 1/python does not read 1
    digitalWrite(motionPin, LOW); //Diag
    
    char noPeople = Serial.read(); /*<----------------------fix with proper pin numbers and syntax--*/
    if (noPeople == 'c'){
      // no person detected in the frame
      digitalWrite(lightPin, LOW); // Turn off lights
      // switch state
      pirState=1;
		
    }
  }
}
