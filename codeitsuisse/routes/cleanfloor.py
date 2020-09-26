import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

class Node:
    def __init__(self, state, atIndex, parent):
        self.state = state
        self.atIndex = atIndex
        self.dirtLv = 0
        if(parent==None):
            for i in state:
                self.dirtLv += i
            self.moves = 0
        else:
            self.moves = parent.moves+1
            if(parent.state[atIndex]==0):
                self.dirtLv = parent.dirtLv+1
            else:
                self.dirtLv = parent.dirtLv-1
        
    def getNextMoves(self):
        nextMoves = []
        currentIndex = self.atIndex
        if(self.atIndex>0):
            # add go-to-left branch
            newState = self.state[:]
            if(newState[currentIndex-1]==0):
                newState[currentIndex-1]=1
            else:
                newState[currentIndex-1]-=1
            nextMoves.append(Node(newState,currentIndex-1,self))

        if(self.atIndex < len(self.state)-1):
            # add go-to-right branch
            newState = self.state[:]
            if(newState[currentIndex+1]==0):
                newState[currentIndex+1]=1
            else:
                newState[currentIndex+1]-=1
            nextMoves.append(Node(newState, currentIndex+1,self))
        
        return nextMoves

@app.route('/clean_floor', methods=['POST'])
def clean():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    data = data["tests"]
    result = {
        "answers": {}
    }
    for key in data:
        result["answers"][key] = minimumMovesToClean(data[key]["floor"])
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def minimumMovesToClean(floorSpace):
    open = []
    start_node = Node(floorSpace,0, None)
    open.append(start_node)
    while len(open)>0:
        open.sort(key=lambda x: (x.dirtLv))
        current_node = open.pop(0)
        # check if current node is goal node
        if(current_node.dirtLv==0):
           return current_node.moves
        
        #we must make a move
        nextMoveStates = current_node.getNextMoves()
        
        for node in nextMoveStates:
            open.append(node)
    return "Path not found"