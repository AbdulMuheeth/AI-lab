n = int(input("Enter the value of n: "))


def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=" ")
        print()

def is_safe(board,r,c):
    
    #column
    for i in range(len(board)):
        if board[i][c] == 1:
            # print(i,"c")
            return False
        # return True
    
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j] == 1:
            # print(i,j,"--")
            return False
        
    # Check lower diagonal on left side
    for i, j in zip(range(r, -1, -1), range(c, len(board), 1)):
        # print(i,j)
        if board[i][j] == 1:
            # print(i,j,"-")
            return False
    
    return True
    

def nqueen(board,row):
        
    if row >= len(board):
        print_board(board)
        return True
    
    for i in range(len(board)):
        
        # print("-----",row,i,"--------",board)
        val = is_safe(board,row,i)
        # print(val)
        
        if val==True:
            
            board[row][i] = 1
            
            if nqueen(board,row+1)==True:
                return True
            
            board[row][i] = 0
        
    return False

board = []
for i in range(n):
    board.append([0]*n)
    
nqueen(board,0)


'''
    0,0  0,1  0,2  0,3
    1,0  1,1  1,2  1,3
    2,0  2,1  2,2  2,3
    3,0  3,1  3,2  3,3

'''