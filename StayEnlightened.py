# Main file where everything will happen
import serial
from MongoInterface import MongoInterface
from peoplecount import PeopleCount
from datetime import datetime

import sys
import time
import os

sys.path.insert(0, './image-capture/')
from Camera import Camera

sys.path.insert(1, './serial_communication/')
import computer_v1 as motion
print("Imported camera")

class StayEnlightened:
    def __init__(self):
        self.jsonPath = os.getcwd() #sys.argv[1]
        self.imgPath = os.getcwd() + '/image-capture/saved_img.jpg' #sys.argv[2]
        print (self.imgPath)
        self.database = MongoInterface(self.jsonPath)
        self.people = PeopleCount(self.imgPath)  #self.imgPath
        self.camera = Camera(0,self.imgPath)
        self.currentPeople = 0
        self.camState = False
        print("Starting...\n\n")

    def loop(self):
        print("Taking pic")
        self.camera.capture()
        self.currentPeople = self.people.count_people()
        self.database.updateCurrent(self.currentPeople)


    def main(self):
        startTime = time.time()
        currentTime = time.time()
        printed = False
        off = False
        updateRate = 10
        port='/dev/tty96B0'
        ser = serial.Serial(port, 9600)
        detected = '0'
        while True:
            if detected == '0':
                detected = motion.read_serial(ser)
            if detected == '1':
                self.camState = True
            
            currentTime = time.time()
            timeDiff = currentTime - startTime
            if timeDiff <= updateRate:
                if not printed:
                    printed = True
                    timeLeft = round(updateRate-timeDiff, 1)
                    print("Updating in:", timeLeft, "seconds")
            
            else:
                dateTime = datetime.now()
                startTime = currentTime
                printed = False

                if self.camState:
                    self.loop()
                    if self.currentPeople > 0:
                        off = False
                    elif self.currentPeople == 0:
                        off = True
                        self.camState = False
                        detected = '0'
                        motion.write_serial(ser)
                        print("cam turned off")
                else:
                    self.camState = motion.check_motion(self.camState, off, detected)
                    if not self.camState:
                        detected = '0'
                print("Motion detecting is:", detected)
                print("Updated at:", dateTime)

light = StayEnlightened()
light.main()
