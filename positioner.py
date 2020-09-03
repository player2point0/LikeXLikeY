import json
import random
import math

#open the json file
with open('data.json') as json_file:
    jsonData = json.load(json_file)


BASE_LIKE_DIS = 1
BASE_BRAND_DIS = 2
GRID_SIZE = 10


def getBrandIndex(jsonData, name):
    index = 0

    while index < len(jsonData["data"]):
        if jsonData["data"][index]["name"] == name:
            return index    
        index += 1
    return -1

def oldWay():        
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

def findLargestBrand():
    brandName = jsonData["data"][0]["name"]
    numLikeBrands = len(jsonData["data"][0]["like"])

    for brandIndex in range(len(jsonData["data"])):
        tempNumLike = len(jsonData["data"][0]["like"])

        if tempNumLike > numLikeBrands:
            numLikeBrands = tempNumLike
            brandName = jsonData["data"][brandIndex]["name"]

    return brandName
            
def positionBrand(brandName, x, y):
    brandIndex = getBrandIndex(jsonData, brandName)

    jsonData["data"][brandIndex]["x"] = x
    jsonData["data"][brandIndex]["y"] = y

def placeLikeBrands(coords, brandName, brandX, BrandY):
    #go through each like brand
    brandIndex = getBrandIndex(jsonData, brandName)

    def placeLikeBrand(likeBrand, x, y):
        #check if the new coordinate clashes with any in the map
        #and if it clashes recalculate        
        
        yield

    for likeBrand in jsonData["data"][brandIndex]["like"]:
        
        #check if it already exists in coords
        for coord in coords:
            if coord["brand"] == likeBrand:
                #if it does place it half way between old and new coords
                newX = ""
                newY = ""
                    
                placeLikeBrand(likeBrand, newX, newY)
                break

        yield



def newWay():
    #find the largest brand
    largestBrand = findLargestBrand()
    #place the largest brand first and the like brands around it
    positionBrand(largestBrand, 0, 0)
    #store the coordinates in a hash map
    coords = [{
        "brand": largestBrand,
        "x": 0,
        "y": 0
    }];
    #call a reursive function to then place the child brands of those brands
    placeLikeBrands(coords, largestBrand)

save = input("save changes (y/N): ")

if save == "y":
    with open('positionData.json', 'w') as outfile:
        json.dump(jsonData, outfile)