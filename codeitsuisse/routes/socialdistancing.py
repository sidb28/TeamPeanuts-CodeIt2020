import logging
import json


from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def comb(n,k):
    numerator = 1
    denom1 = denom2 = 1
    for i in range(1,n+1):
        numerator*=i
        if(i==k):
            denom1 = numerator
        if(i==n-k):
            denom2 = numerator
    return numerator/(denom1*denom2)

@app.route('/social_distancing', methods=['POST'])
def social_distancing_evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    testVals = data.get("tests")
    result = []
    answer = {"answers": {}}
    for key in testVals:
        x=testVals[key]["seats"]
        y=testVals[key]["people"]
        z=testVals[key]["spaces"]
        answer["answers"][key] = comb(x-(z*(y-1)), y)    
    logging.info("My result :{}".format(result))
    return json.dumps(answer)
