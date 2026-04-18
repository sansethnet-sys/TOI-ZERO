X , Y = 0 , 0
for it in input():
    if it=="N": Y+=1
    elif it=="E": X+=1
    elif it=="W": X-=1
    else: Y-=1
print(X,Y,abs(X)+abs(Y))