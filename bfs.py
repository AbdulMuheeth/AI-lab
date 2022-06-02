from collections import defaultdict



class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def bfs(self,start):
        queue,visited = [],[]
        
        
        start_node = start
        queue.append(start_node)
        visited.append(start_node)
        
        while(len(queue)>0):
            parent = queue.pop(0)
            print(parent,end=" ")
            neighbour_nodes = self.graph[parent]
            
            for node in neighbour_nodes:
                if node not in visited:
                    queue.append(node)
                    visited.append(node)
        

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

print("BFS for the graph is: ")
g.bfs(0)