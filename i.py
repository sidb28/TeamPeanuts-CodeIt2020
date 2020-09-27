def getSearchResult(searchItem, listOfItems):
    finalList = []

    for item in listOfItems:
        finalList.append(computeObject(searchItem,item))

    finalList = sorted(finalList, lambda x: (x["num"],x["original"]))
    listToReturn = []
    for i in finalList:
        listToReturn.append(finalList["stringVal"])
    return listToReturn

def computeObject(searchItem,item):
    itemCopy = item
    return {
        "num": 1,
        "original": item,
        "stringVal": "-Sams+ung"
    }