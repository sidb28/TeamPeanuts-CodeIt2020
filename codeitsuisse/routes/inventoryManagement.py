import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/inventory-management', methods=['POST'])
def inventoryManagement():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for case in data:
        result.append({"searchItemName":case["searchItemName"],"searchResult": getSearchResult(case["searchItemName"],case["items"])})
    logging.info("My result :{}".format(result))
    return jsonify(result)

def getSearchResult(s1, items):
    searchResults = []
    resultCosts = []
    s1=s1.lower()
    for s in items:
        s2 = s.lower()
        k = k1 = k2 = num_operations = 0
        res = ''
        l1 = len(s1)
        l2 = len(s2)
        while(k1<l1 and k2<l2):
            if s1[k1] == s2[k2]:
                res+=s1[k1]
                k1 += 1
                k2 += 1
            else:
                num_operations += 1
                try:
                    p = s1.index(" ", k1)
                except ValueError:
                    p = len(s1)
                if s2[k2] not in s1[k1:p]:
                    res += "+" + s2[k2]
                    k2 += 1
                else:
                    res += "-" + s1[k1]
                    k1 += 1

        for i in range(k1,l1):
            res += "-" + s1[i]
        
        for i in range(k2,l2):
            res += "+" + s2[i]

        while (k < len(res)-4):
            substring = res[k:k+3]
            if ( "+" in substring and "-" in substring and substring.index("+")<substring.index("-") ):
                res = res[0:k]+res[k+1]+res[k+4:]
                num_operations -= 1
            k+=1

        searchResults.append({
            "originalString": s,
            "newString": res,
            "cost": num_operations
        })

    searchResults.sort(key = lambda x: (x["cost"],x["originalString"]))
    finalList = []
    
    for result in searchResults[:min(10,len(searchResults))]:
      finalList.append(result["newString"])  

    # finalList.append(searchResults[i]["originalString"])
    return finalList        