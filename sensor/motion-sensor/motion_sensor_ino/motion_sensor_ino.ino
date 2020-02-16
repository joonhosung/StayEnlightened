//This code will allow the PIR motion sensor to send updates to:
// 1. Turn on the camera if motion/people are detected
// 2. Turn off the camera if no motion is detected.

int lightPin = 11; //The "lights" to be controlled
int motionPin = 13; //Diagnostic Output pin - if motion detected
int inputPin = 2; //Input pin - the PIR sensor
int pirState = LOW; //No motion at start
int movement = 0; //Pin status (HIGH or LOW)

void setup() {
  pinMode(motionPin, OUTPUT); 
  pinMode(lightPin, OUTPUT);
  pinMode(inputPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  movement = digitalRead(inputPin); //Read input 
  
  if (movement == HIGH) { //If motion detected:
    digitalWrite(lightPin, HIGH); //Turn on the lights.
    digitalWrite(motionPin, HIGH); //Turn diagnostic output ON
    
    //If previous state was "no motion detected", then change state to "motion detected"
    if (pirState == LOW) {
      Serial.println(1); //Send serial data to python -> computer.py, which will tell the camera to turn on and take pictures in OpenCV
      //Serial.println("Motion detected. Switching to camera.");
      pirState = HIGH; //Change state.

      //Arduino then enters read mode (starts waiting for Jun Ho’s python/OpenCV to say when NO PEOPLE are detected by the camera)
      //Not writing to python at this time (unidirectional transfer)
      
      //CHECK THIS LINEEEEEEEEEEEEE
      int num = Serial.read(); //read data from python - how many people in field of view of camera
      while (num > 0) { //need this while loop? or just the if statement below?
        //People
      }
      if (num == 0) { //If no one present, then start reading from the PIR sensor again.
        //Turn off the lights
        digitalWrite(lightPin, LOW); //Turn off the lights.
        //naturally leaves this loop. And loops main fn. (switches state)
      }
      
    }
    
  } else { //Motion not detected:
    digitalWrite(motionPin, LOW); //Turn diagnostic output OFF
    
    //If last state was "motion detected", change to "no motion detected"
    if (pirState == HIGH){
      Serial.println(0);
      //Serial.println("No motion. Camera off.");
      pirState = LOW; //Change state
    }
  }
  
  
}
