//This code will allow the PIR motion sensor to send updates to:
// 1. Turn on the camera if motion/people are detected
// 2. Turn off the camera if no motion is detected.

int motionPin = 13; //Output pin - if motion detected
int inputPin = 2; //Input pin - the PIR sensor
int pirState = LOW; //No motion at start
int movement = 0; //Pin status (HIGH or LOW)

void setup() {
  pinMode(motionPin, OUTPUT); 
  pinMode(inputPin, INPUT);
  Serial.begin(9600);
}

void loop() {

  movement = digitalRead(inputPin); //Read input 
  if (movement == HIGH) { //If motion detected:
    digitalWrite(motionPin, HIGH); //Turn output ON
    if (pirState == LOW) {
      Serial.println(1);
      //Serial.println("Motion detected. Switching to camera.");
      pirState = HIGH; //Change state.
    }
  } else { //Motion not detected:
    digitalWrite(motionPin, LOW); //Turn output OFF
    if (pirState == HIGH){
      Serial.println(0);
      //Serial.println("No motion. Camera off.");
      pirState = LOW;
    }
  }
}
