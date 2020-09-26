import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def fruit():
    weights = {
        "maApple": 1,
        "maWatermelon": 2,
        "maAvocado": 3
    }
    data = json.loads(request.data.decode("utf-8"))
    logging.info("data sent for evaluation {}".format(data))
    print(data)
    result = 0
    logging.info("My result :{}".format(result))
    return json.dumps(result)



