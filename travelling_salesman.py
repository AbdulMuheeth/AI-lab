from sys import maxsize
from itertools import permutations

def bruteforce(graph,s):
    
    vertices = []
    for i in range(len(graph)):
        if i!=s:
            vertices.append(i)
            
    min_path_cost = maxsize
    all_paths = permutations(vertices)
    
    for path in all_paths:
        cur_weight = 0
        # cur_weight+= graph[s][path[0]]
        # for vertex in range(len(path)-1):
        #     cur_weight += graph[vertices[vertex]][vertices[vertex+1]]
        # cur_weight+= graph[path[-1]][s]
        k = s
        for j in path:
            cur_weight += graph[k][j]
            k = j
        cur_weight += graph[k][s]
        min_path_cost = min(cur_weight,min_path_cost)
                
    return min_path_cost

graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
print(bruteforce(graph,0))