import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def fruit():
    weights = {
        "maApple": 50,
        "maWatermelon": 30,
        "maAvocado": 25,
        "maRamubutan": 10,
        "maPineapple": 60,
        "maPomegranate": 10
    }
    data = json.loads(request.data.decode("utf-8"))
    logging.info("data sent for evaluation {}".format(data))
    result = 0
    for key in data:
        weightOfFruit = 0
        try:
            weightOfFruit = weights[key]
        except:
            print(key)
            weightOfFruit = 50
        finally:
            result += data[key]*weightOfFruit
    print(result)
    logging.info("My result :{}".format(result))
    return json.dumps(result)



