import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

class Node:
    def __init__(self, position, parent):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self,other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


@app.route('/supermarket', methods=['POST'])
def mazeSolve():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    data = data["tests"]
    result = {
        "answers": {}
    }
    for key in data:
        result["answers"][key] = minimumMovesToReach(data[key]["maze"], data[key]["start"], data[key]["end"])
    logging.info("My result :{}".format(result))
    return jsonify(result)

def minimumMovesToReach(maze, start,end):
    open = []
    closed = []
    start_node = Node(start,None)
    goal_node = Node(end,None)
    open.append(start_node)
    while len(open)>0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)

        # check if current node is goal node
        if(current_node==goal_node):
            moves = 1
            while current_node!=start_node:
                moves+=1
                current_node = current_node.parent
            return moves
        
        x= current_node.position[0]
        y=current_node.position[1]
        #we must make a move
        nextMoves = []
        if(x>0):
            nextMoves.append([x-1, y])
        if(x<len(maze[y])-1):
            nextMoves.append([x+1, y])
        if(y>0):
            nextMoves.append([x, y-1])
        if(y<len(maze)-1):
            nextMoves.append([x, y+1])
        
        for node in nextMoves:
            if(maze[node[1]][node[0]]==1):
                continue
            neighbour = Node(node, current_node)
            if(neighbour in closed):
                 continue
            neighbour.g = abs(neighbour.position[0]-start_node.position[0]) + abs(neighbour.position[1]-start_node.position[1])
            neighbour.h = abs(neighbour.position[0]-goal_node.position[0]) + abs(neighbour.position[1]-goal_node.position[1])
            neighbour.f = neighbour.g + neighbour.h

            if(add_to_open(neighbour, open)):
                open.append(neighbour)

    return -1

def add_to_open(neighbour, open):
    for node in open:
        if(neighbour==node and neighbour.f>=node.f):
            return False
    return True