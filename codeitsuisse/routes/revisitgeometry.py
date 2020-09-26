import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/revisitgeometry', methods=['POST'])


def intersection():
    data = request.get_json()
    #logging.info("data sent for evaluation {}".format(data))
    shapeCoord = data.get("shapeCoordinates")
    lineCoord = data.get("lineCoordinates")
    result = set()
    X1 = lineCoord[0]['x']
    Y1 = lineCoord[0]['y']
    X2 = lineCoord[1]['x']
    Y2 = lineCoord[1]['y']
    for i in range(len(shapeCoord)):
        j = 0 if i == len(shapeCoord) - 1 else i+1
        X3 = shapeCoord[i]['x']
        Y3 = shapeCoord[i]['y']
        X4 = shapeCoord[j]['x']
        Y4 = shapeCoord[j]['y']

        if (X1-X2)*(Y3-Y4)-(Y1-Y2)*(X3-X4)==0:
            continue
        X = ((X1*Y2-Y1*X2)*(X3-X4)-(X1-X2)*(X3*Y4-Y3*X4)) / ((X1-X2)*(Y3-Y4)-(Y1-Y2)*(X3-X4))
        Y = ((X1*Y2-Y1*X2)*(Y3-Y4)-(Y1-Y2)*(X3*Y4-Y3*X4)) / ((X1-X2)*(Y3-Y4)-(Y1-Y2)*(X3-X4))
    
        if (X-X3)*(X-X4) < 0 and (Y-Y3)*(Y-Y4) < 0:
            result.add((X,Y))
        
    listOfCoordinates = []
    for coord in result:
        listOfCoordinates.append(jsonify({
            "x": coord[0],
            "y": coord[1]
        }))
   # logging.info("My result :{}".format(listOfCoordinates))
    return json.dumps(listOfCoordinates)
