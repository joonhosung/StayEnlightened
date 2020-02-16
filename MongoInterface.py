import pymongo as mongo
from pprint import pprint
import json
import os

def initializeSpace():
    path = os.getcwd()

    # Open json file
    for f_name in os.listdir(path):
        if f_name.startswith('room') and f_name.endswith('.json'):
            jsonFile = f_name


    # Convert json file to easy-to-use variables
    with open(jsonFile) as json_file:
        data = json.load(json_file)
        building = data['space']['building']
        area = data['space']['area']
        maxSeats = data['space']['max']


    # Set MongoDB variables    
    client = mongo.MongoClient("mongodb+srv://StayEnlightened:Myhal@numbers-iox3o.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Workspaces                # Workspaces db
    currentBuilding = db[building]        # find or add building collection

    # Update area document in building collection
    query = {"name", area}
    newData = {"name": area, "max": maxSeats}
    result = currentBuilding.update_one(
        query, 
        {"$set": newData},
        upsert=True)

    # if result.matched_count == 0 :
    #     currentBuilding.find_and_modify(query, update= )
    # print("modified count:", result.modified_count) 


    # print every document (area) in Workspaces db
    cursor = currentBuilding.find({})        
    #print(currentBuilding)
    for j in currentBuilding.find():
        pprint(j)
