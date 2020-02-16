import pymongo as mongo
from pprint import pprint
import json
import os
class MongoInterface:
    
    client = mongo.MongoClient("mongodb+srv://StayEnlightened:Myhal@numbers-iox3o.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Workspaces                # Workspaces db

    # path = current directory
    def __init__(self, path):
        #path = os.getcwd()

        # Open json file
        for f_name in os.listdir(path):
            if f_name.startswith('room') and f_name.endswith('.json'):
                jsonFile = f_name


        # Convert json file to easy-to-use variables
        with open(jsonFile) as json_file:
            data = json.load(json_file)
            self.building = data['space']['building']
            self.area = data['space']['area']
            self.maxSeats = data['space']['max']

        # Set MongoDB variables    
        
        currentBuilding = self.db[self.building]        # find or add building collection
        # Update area document in building collection
        self.query = {"name": self.area}
        newData = {"name": self.area, "max": self.maxSeats}
        currentBuilding.update_one(
            self.query, 
            {"$set": newData},
            upsert=True)

        # if result.matched_count == 0 :
        #     currentBuilding.find_and_modify(query, update= )
        # print("modified count:", result.modified_count) 

        # print every document (area) in Workspaces db        
        #print(currentBuilding)
        for j in currentBuilding.find():
            pprint(j)


    # Update current number of humans in study space
    def updateCurrent(self, number):
        building = self.db[self.building] 
        newData = {"current": number}
        
        print("number of people:", number)
        building.update_one(
            self.query, 
            {"$set":newData}, 
            upsert=True)

