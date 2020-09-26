import logging
import json


from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])

def comb(n,k):
    ans=1
    for i in range(k):
        ans = ans*(n-i)
    return ans

def social_distancing_evaluate():
    data = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    testVals = data.get("tests")
    result = []
    for i in range(len(testVals)):
        x=testVals[str(i)]["seats"]
        y=testVals[str(i)]["people"]
        z=testVals[str(i)]["spaces"]
        result.append(comb(x-(z*(y-1)), y))
    
    answer = {"answers": {}}
    for p, val in enumerate(result):
        answer["answers"][str(p)] = val
    
    #logging.info("My result :{}".format(result))
    return json.dumps(answer)