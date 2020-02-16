/* Sensor Cluster using Sensors Mezzaine on DragonBoard410c

 * Author: Radhika Paralkar

 * Copyright (c) 2017 Linaro Ltd.

 * All rights reserved.

 ********************************

 * 

 * A0 --> Light Sensor

 * A1 --> Temperature Sensor

 * A2 --> Sound Sensor

 * D4 --> Touch Sensor Module

 * D5 --> Button

 * D6 --> Rotary Angle Sensor

 */



//Define the pins for each sensor



const int lightSensor = A0;

const int rotarySensor = 0;





/*Setup runs only once during the program. Set all sensor pins as 

Input and set the baud rate for serial for printing on the serial port*/



void setup()

{

    Serial.begin(9600);

    pinMode(lightSensor, INPUT);           


}



/* The light, temperature and sound sensors give analog readings, hence 

they have been placed on the analog pins and we use analogRead to read 

their values. Similarly, the button and touch sensor will give digital 

values. The rotary angle sensor would ideally provide analog values, 

however since we have only three analog pins, we connect the rotary angle 

sensor onto a digital pin*/

  

void loop() 

{

  	int light_sensorVal = analogRead(lightSensor);

	int motion_sensorVal = digitalRead(rotarySensor);



	Serial.println("Sensor      | Value     ");

	Serial.println("--------------------");



	Serial.print("Light       | ");

	Serial.println(light_sensorVal);



	Serial.print("Motion      | ");

	Serial.println(motion_sensorVal);

	delay(400);



	Serial.println("");

}
