from math import ceil
X , Y = map(int,input().split())
sc = X*(X+2)//4+X%2-Y
if sc<0: print(-1)
else:
    if X%2: print(X//2+1-int(sc**0.5))
    else: print(ceil(X/2-(4*sc+1)**0.5/2+0.5))