# Print square in spiral form
import numpy as np
import math
sq=int(input())
n=int(math.sqrt(sq))
a=np.ones((n,n),dtype=np.int)
i=j=0
dir='R'
num=1
TB=LB=0
RB=n-1
BB=n-1
while num<=sq:
    a[i,j]=num
    #print((i,j),a[i,j])
    #print(TB,RB,BB,LB)
    num+=1
    if dir=='R':
        if j<RB:
            j=j+1
        else:
            i=i+1
            dir='B'
            TB=TB+1
    elif dir=='B':
        if i<BB:
            i=i+1
        else:
            j=j-1
            dir='L'
            RB=RB-1
    elif dir=='L':
        if j>LB:
            j=j-1
        else:
            i=i-1
            dir='T'
            BB=BB-1
    else:
        if i>TB:
            i=i-1
        else:
            j=j+1
            dir='R'
            LB=LB+1
print(a)
        
    

