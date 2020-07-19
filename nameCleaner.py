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


brandIndex = 0

while brandIndex < len(jsonData["data"]):
    brandName = jsonData["data"][brandIndex]["name"]
    jsonData["data"][brandIndex]["name"] = cleanName(brandName)

    likeIndex = 0

    while likeIndex < len(jsonData["data"][brandIndex]["like"]):
        likeName = jsonData["data"][brandIndex]["like"][likeIndex]
        jsonData["data"][brandIndex]["like"][likeIndex] = cleanName(likeName)

        likeIndex += 1
    brandIndex += 1


save = input("save changes (y/n): ")

if save == "y":
    with open('cleanNameData.json', 'w') as outfile:
        json.dump(jsonData, outfile)