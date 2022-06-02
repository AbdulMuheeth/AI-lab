from collections import defaultdict



class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def dfsUtil(self,node,visited):
        visited.add(node)
        print(node,end=" ")
        
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                    self.dfsUtil(neighbour,visited)
        
    
    def dfs(self,start):
        visited = set()        
        self.dfsUtil(0,visited)
        


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 4)
g.addEdge(2, 4)
g.addEdge(3, 4) 

'''
        0
      / | \
     1  2  3
     \  |  /
        4
'''

print("DFS for the graph is: ")
g.dfs(0)