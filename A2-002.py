bt = dict({})
for i in range(int(input())):
    x , y = map(int,input().split())
    if y-x not in bt: bt[y-x]=[x,x]
    if y+x not in bt: bt[y+x]=[x,x]
    bt[y-x]=[min(bt[y-x][0],x),max(bt[y-x][1],x)]
    bt[y+x]=[min(bt[y+x][0],x),max(bt[y+x][1],x)]
print(max([xm-nm for nm,xm in bt.values()]))