rx , wx , ct = "" , -2**31 , 0
for i in range(int(input())):
    R , W = input().split()
    W = int(W)
    ct += (W>15)
    if W>wx : rx , wx = R , W
print(ct,"\n"+rx,wx)
