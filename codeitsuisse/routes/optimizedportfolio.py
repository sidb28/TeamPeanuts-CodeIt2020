import logging
import json


from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def getKey(dictionary, value):
    for key, i in dictionary.items():
        if value == i:
            return key

def calcOHR(cr, spd, fpd):
    return cr*(spd/fpd)

def futCont(ohr, portVal, fp, notVal):
    return (ohr*portVal)/(fp*notVal)

@app.route('/optimizedportfolio', methods=['POST'])
def portfolio_evaluate():
    data = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    inputVal = data.get("inputs")
    ohr = {}
    futVol = {}
    numfut = {}
    for i in range(len(inputVal)):
        portfolioVal = inputVal[i]["Portfolio"]["Value"]
        SpotVol = inputVal[i]["Portfolio"]["SpotPrcVol"]

        for j in range(len(inputVal[i]["IndexFutures"])):
            name = inputVal[i]["IndexFutures"][j]["Name"]
            cr = inputVal[i]["IndexFutures"][j]["CoRelationCoefficient"]
            t1 = inputVal[i]["IndexFutures"][j]["FuturePrcVol"]
            futVol[name]=t1
            futPrice = inputVal[i]["IndexFutures"][j]["IndexFuturePrice"]
            notional = inputVal[i]["IndexFutures"][j]["Notional"]
            t2 = calcOHR(cr, SpotVol, futVol[name])
            ohr[name]=round(t2,3)
            t3 = futCont(ohr[name], portfolioVal, futPrice, notional)
            numfut[name]=round(t3)

        minOHR = min(ohr.values())
        minOHRkey = getKey(ohr, minOHR)
        minfutVol = min(futVol.values())
        minfutVolkey = getKey(futVol, minfutVol)
        minNumFut = min(numfut.values())
        minNumFutkey = getKey(numfut, minNumFut)

        if minOHRkey is minfutVolkey:
            result = {"outputs": [{
                "HedgePositionName" : minOHRkey, 
                "OptimalHedgeRatio" : minOHR, 
                "NumFuturesContract" : numfut[minOHRkey]
                }]}
            
        else:
            result = {"outputs": [{
                "HedgePositionName" : minNumFutkey, 
                "OptimalHedgeRatio" : ohr[minNumFutkey], 
                "NumFuturesContract" : minNumFut
                }]}
       
    #logging.info("My result :{}".format(result))
    return json.dumps(result)
