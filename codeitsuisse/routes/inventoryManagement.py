import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


def getSearchResult(searchItem, listOfItems):

    finalList = ["abc"]
    finalList = sorted(finalList, lambda x: (x["num"],x["original"]))
    listToReturn = []
    for i in finalList:
        listToReturn.append(finalList["stringVal"])
    return listToReturn



@app.route('/inventory-management', methods=['POST'])
def inventoryManagement():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for case in data:
        result.append({"searchItemName":case["searchItemName"],"searchResult": getSearchResult(case["searchItemName"],case["items"])})
    logging.info("My result :{}".format(result))
    return json.dumps(result)
