n , m = map(int,input().split())
tp = ["-"*m] + [input().split() for i in range(n)]
for i in range(1,1+n):
    for j in range(m):
        if tp[i-1][j]=='*' : print("*",end=" ")
        else : print(tp[i][j],end=" ")
    print()