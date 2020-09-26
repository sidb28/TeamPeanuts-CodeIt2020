class Graph:

  def __init__(self, r, c, g):
    self.row = r
    self.col = c
    self.graph = g

  def is_in_chain(self, i , j, visited):
    if (i>=0 and i<self.row and j>=0 and j<self.col and self.graph[i][j] and not visited[i][j]):
      return True 

  def depth_first_search(self, i, j, visited):
    r_num = [-1, -1, -1,  0, 0,  1, 1, 1]
    c_num = [-1,  0,  1, -1, 1, -1, 0, 1]

    visited[i][j] = True

    for k in range(8):
      if self.

  