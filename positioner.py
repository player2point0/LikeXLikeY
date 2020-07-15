import json
import random
import math

#open the json file
with open('data.json') as json_file:
    jsonData = json.load(json_file)





# todo add a grid 
# todo add collison preventiion
# todo add clustering of brands based on shared connections



#for each like brand check if it has coordinates
#if it does place it half way between the coordinated and the coordinates of the main brand
#else assign a random coordinate


brandIndex = 0

while brandIndex < len(jsonData["data"]):

    brandX = random.random() * 5
    brandY = random.random() * 5

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

        #find like brand entry
        likeName = jsonData["data"][brandIndex]["like"][likeIndex]

        likeBrandIndex = 0

        while likeBrandIndex < len(jsonData["data"]):
            if jsonData["data"][likeBrandIndex]["name"] == likeName:

                #random polar coordinate near the brand
                angle = random.random() * 3.14 * 2
                length = random.random() * 2
                
                likeX = brandX + (length * math.cos(angle))
                likeY = brandY + (length * math.sin(angle))

                # if not position assign the random polar coordinate
                if "x" not in jsonData["data"][likeBrandIndex] or "y" not in jsonData["data"][likeBrandIndex] or jsonData["data"][likeBrandIndex]["x"] and jsonData["data"][likeBrandIndex]["y"]:
                    jsonData["data"][likeBrandIndex]["x"] = likeX
                    jsonData["data"][likeBrandIndex]["y"] = likeY

                #else place it half way between the coordinated and the coordinates of the main brand
                else:
                    jsonData["data"][likeBrandIndex]["x"] = (jsonData["data"][likeBrandIndex]["x"] + likeX) / 2
                    jsonData["data"][likeBrandIndex]["y"] = (jsonData["data"][likeBrandIndex]["y"] + likeY) / 2
        
            likeBrandIndex += 1
        likeIndex += 1
    brandIndex += 1


save = input("save changes (y/N): ")

if save == "y":
    with open('positionData.json', 'w') as outfile:
        json.dump(jsonData, outfile)