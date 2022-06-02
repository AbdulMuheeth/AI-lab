
def t_of_hanoi(n,from_p,to_p,aux):
    
    if n == 1:
        print("move {} from {} to {}".format(1,from_p,to_p))
        return
    
    t_of_hanoi(n-1,from_p,aux,to_p)
    print("move {} from {} to {}".format(n,from_p,to_p))
    t_of_hanoi(n-1,aux,to_p,from_p)
    
t_of_hanoi(4,"A","B","C")
    