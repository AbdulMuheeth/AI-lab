class Puzzle:
    
    def solve(self,mat):
        
        flatten,d = [],{}
        
        for i in mat:
            flatten += i
        
        flatten = tuple(flatten)    
        d[flatten] = 0
        
        if flatten == (1,2,3,4,8,5,0,7,6):
            return 0
        
        return self.get_paths(d)
    
    def get_paths(self,d):
        
        cnt = 0
        
        while True:
            
            to_extend = [x for x in d if d[x] == cnt]
                
            print(to_extend)
            if len(to_extend) == 0:
                return -1
            
            for i in to_extend:
                res = self.find_next(i)
                
                for j in res:
                    if j not in d:
                        d[j] = cnt+1
                    if j == (1,2,3,4,8,5,0,7,6):
                        return cnt+1
                    
            cnt+=1
                

    def find_next(self,nodes):
        moves  = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4: [1, 3, 5, 7],5: [2, 4, 8],6: [3, 7],7: [4, 6, 8],8: [5, 7]}
        
        
        idx = nodes.index(0)
        res = []
        for move in moves[idx]:
            tmp = list(nodes)
            tmp[move],tmp[idx] = tmp[idx],tmp[move]
            res.append(tuple(tmp))
        
        return res
            
mat = [[1,2,3],[4,5,6],[7, 8, 0]]
puz = Puzzle()
print(puz.solve(mat))
