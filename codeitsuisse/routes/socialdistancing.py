import logging
import json
import math

from flask import request, jsonify
from math import comb

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/social_distancing', methods=['POST'])

def evaluate():
    data = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    testVals = data.get("tests")
    result = []
    for i in range(len(testVals)):
        x=testVals[i]["seats"]
        y=testVals[i]["people"]
        z=testVals[i]["spaces"]
        result = comb(y-z(x-1), x)
    
    answer = {}
    for p, val in enumerate(result):
        answer["answers"].append({str(p):val})
    
    #logging.info("My result :{}".format(result))
    return json.dumps(answer)