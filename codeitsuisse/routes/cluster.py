import json

from flask import request, jsonify;

from codeitsuisse import app;

class Graph:

  def __init__(self, r, c, g):
    self.row = r
    self.col = c
    self.graph = g

  def is_in_chain(self, i , j, visited):
    if (i>=0 and i<self.row and j>=0 and j<self.col and self.graph[i][j]!="*" and not visited[i][j]):
      return True 

  def depth_first_search(self, i, j, visited):
    r_num = [-1, -1, -1,  0, 0,  1, 1, 1]
    c_num = [-1,  0,  1, -1, 1, -1, 0, 1]

    visited[i][j] = True

    for k in range(8):
      if self.is_in_chain(i+r_num[k], j+c_num[k], visited):
        self.depth_first_search(i+r_num[k], j+c_num[k], visited)

  def cluster_count(self):
    visited = [[False for j in range(self.col)]for i in range(self.row)] 
  
    count = 0
    for i in range(self.row):
      for j in range(self.col):
        if visited[i][j] == False and self.graph[i][j] == "1":
          self.depth_first_search(i, j, visited)
          count += 1
    
    return count
   

  @app.route('/cluster', methods=['POST'])
  def cluster():
    data = request.get_json()
    
    row = len(data) 
    col = len(data[0]) 
    graph = Graph(row, col, data) 
    clusters = graph.cluster_count()

    output = {"answer": clusters}
    return jsonify(output)
