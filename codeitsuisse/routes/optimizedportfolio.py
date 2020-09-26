import logging
import json


from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def calcOHR(cr, spd, fpd):
    return cr*(spd/fpd)

def futCont(ohr, portVal, fp, notVal):
    return (ohr*portVal)/(fp*notVal)

@app.route('/optimizedportfolio', methods=['POST'])
def portfolio_evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputVal = data.get("inputs")
    inp = inputVal[0]

    ohr = {}
    numfut = {}
    
    portfolioVal = inp["Portfolio"]["Value"]
    SpotVol = inp["Portfolio"]["SpotPrcVol"]

    minOHR = 0
    minfutVol = inp["IndexFutures"][0]["FuturePrcVol"]
    minfutVolkey = inp["IndexFutures"][0]["Name"]
    minOHRkey = inp["IndexFutures"][0]["Name"]
    minNumFutkey = inp["IndexFutures"][0]["Name"]

    for j in range(len(inp["IndexFutures"])):
        temp = inp["IndexFutures"][j]

        name = temp["Name"]
        cr = temp["CoRelationCoefficient"]

        t1 = temp["FuturePrcVol"]
        
        if t1 < minfutVol :
            minfutVol = t1
            minfutVolkey = name
        
        futPrice = temp["IndexFuturePrice"]
        notional = temp["Notional"]

        t2 = calcOHR(cr, SpotVol, t1)
        if j == 0:
            minOHR = round(t2,3)
        elif t2 < minOHR:
            minOHR = round(t2,3)
            minOHRkey = name
        ohr[name] = round(t2,3)

        t3 = futCont(ohr[name], portfolioVal, futPrice, notional)
        if j == 0:
            minNumFut = round(t3)
        elif t3 < minOHR:
            minNumFut = round(t3)
            minNumFutkey = name
        numfut[name]=round(t3)

    if minOHRkey == minfutVolkey:
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
       
    logging.info("My result :{}".format(result))
    return json.dumps(result)
