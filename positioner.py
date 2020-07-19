import json
import random
import math

#open the json file
with open('data.json') as json_file:
    jsonData = json.load(json_file)



def getBrandIndex(jsonData, name):
    index = 0

    while index < len(jsonData["data"]):
        if jsonData["data"][index]["name"] == name:
            return index    
        index += 1
    return -1

#todo refactor 

# todo add a grid 
# todo ensure a given brnd cannot excede its grid block
# todo add collison preventiion
# todo add clustering of brands based on shared connections

BASE_LIKE_DIS = 1
BASE_BRAND_DIS = 2
GRID_SIZE = 10


#get the total number of brands with like brands - this is the number of brand clusters
numBrandsWithLikeBrands = 0

for i in range(len(jsonData["data"])):
    if len(jsonData["data"][i]["like"]) > 0:
        numBrandsWithLikeBrands += 1


brandIndex = 0

while brandIndex < len(jsonData["data"]):

    #brandAngle = (brandIndex / len(jsonData["data"][brandIndex]["like"])) * 3.14 * 2
    #brandLength = BASE_LIKE_DIS(numBrandsWithLikeBrands) + random.random() / 2

    #todo use polar coordinates again
    brandX = random.random() * GRID_SIZE
    brandY = random.random() * GRID_SIZE

    #for each brand check if it has coordinates
    #if not position it randomly
    if "x" not in jsonData["data"][brandIndex] or "y" not in jsonData["data"][brandIndex] or not jsonData["data"][brandIndex]["x"] or not jsonData["data"][brandIndex]["y"]:
        jsonData["data"][brandIndex]["x"] = brandX
        jsonData["data"][brandIndex]["y"] = brandY
    
    else:
        brandX = jsonData["data"][brandIndex]["x"]
        brandY = jsonData["data"][brandIndex]["y"]


    #for each like brand check if it has coordinates
    likeIndex = 0

    while likeIndex < len(jsonData["data"][brandIndex]["like"]):

        #find like brand entry in the like brand names array
        likeName = jsonData["data"][brandIndex]["like"][likeIndex]
        likeBrandIndex = getBrandIndex(jsonData, likeName)

        if likeBrandIndex > -1:
            #random polar coordinate near the brand
            angle = (likeIndex / len(jsonData["data"][brandIndex]["like"])) * 3.14 * 2
            length = BASE_LIKE_DIS
            
            likeX = brandX + (length * math.cos(angle))
            likeY = brandY + (length * math.sin(angle))

            # if not position assign the random polar coordinate
            if "x" not in jsonData["data"][likeBrandIndex] or "y" not in jsonData["data"][likeBrandIndex] or jsonData["data"][likeBrandIndex]["x"] and jsonData["data"][likeBrandIndex]["y"]:
                jsonData["data"][likeBrandIndex]["x"] = likeX
                jsonData["data"][likeBrandIndex]["y"] = likeY

            #else place it half way between the coordinated and the coordinates of the main brand
            else:
                #todo check this
                jsonData["data"][likeBrandIndex]["x"] = (jsonData["data"][likeBrandIndex]["x"] + likeX) / 2
                jsonData["data"][likeBrandIndex]["y"] = (jsonData["data"][likeBrandIndex]["y"] + likeY) / 2
        
        likeIndex += 1
    brandIndex += 1


save = input("save changes (y/N): ")

if save == "y":
    with open('positionData.json', 'w') as outfile:
        json.dump(jsonData, outfile)