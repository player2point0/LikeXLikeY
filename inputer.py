import json
import re


def cleanName(name):
    #convert to lowercase
    lowercaseName = name.lower()
    #convert '+', '&' to ' and '
    plusName = lowercaseName.replace('+', ' and ')
    ampersandName = plusName.replace('&', ' and ')
    #remove any special characters and excess spaces
    specialCharName = re.sub(r'\W+', ' ', ampersandName)
    return specialCharName

#open the json file
with open('data.json') as json_file:
    jsonData = json.load(json_file)

while True:

    #read in new name
    inputName = input("enter name or press enter to exit: ")

    if not inputName:
        break

    brandIndex = 0
    brandExists = False

    #check if name exists
    while brandIndex < len(jsonData["data"]):

        if jsonData["data"][brandIndex]["name"] == inputName:
            brandExists = True
            break

        brandIndex += 1

    if not brandExists:
        jsonData["data"].append({
            "name": inputName,
            "url": "",
            "like": []
        })

    #read in new like names
    likeNames = input("enter comma seperated like names: ").split(",")
    #todo clean and format the like names
    
    #update the like brands
    jsonData["data"][brandIndex]["like"].extend(likeNames)
    #check if like names exists
    for likeName in likeNames:

        brandIndex = 0
        brandExists = False

        while brandIndex < len(jsonData["data"]):

            if jsonData["data"][brandIndex]["name"] == likeName:
                brandExists = True
                break

            brandIndex += 1

        if not brandExists:
            jsonData["data"].append({
                "name": likeName,
                "url": "",
                "like": []
            })


save = input("save changes (y/n): ")

if save == "y":
    with open('data.json', 'w') as outfile:
        json.dump(jsonData, outfile)