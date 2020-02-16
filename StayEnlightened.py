# Main file where everything will happen

from MongoInterface import MongoInterface
from peoplecount import PeopleCount
from datetime import datetime
import sys
import time
import os



class StayEnlightened:
    def __init__(self):
        self.jsonPath = os.getcwd() #sys.argv[1]
        self.imgPath = os.getcwd() #sys.argv[2]
        self.database = MongoInterface(self.jsonPath)
        self.people = PeopleCount('myhal/myhal1.jpg')  #self.imgPath
        self.currentPeople = 0
        print("Starting...\n\n")

    def loop(self):
        self.currentPeople = self.people.count_people()
        self.database.updateCurrent(self.currentPeople)


    def main(self):
        startTime = time.time()
        currentTime = time.time()
        printed = False
        off = False
        updateRate = 10
        
        while not off:
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
                self.loop()
                print("Updated at:", dateTime)

light = StayEnlightened()
light.main()