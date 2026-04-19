N , M = map(int,input().split())
tb = [[0]*(M+2) for it in range(N+2)]
for it in range(int(input())):
    r , c = map(int,input().split())
    tb[r+1][c+1] , r , c = -9 , 1+r , 1+c
    for i in range(-1,2):
        for j in range(-1,2): tb[i+r][j+c]+=1
for i in range(1,1+N):
    for j in range(1,1+M):
        if tb[i][j]<0 : print(end="x ")
        else : print(tb[i][j],end=' ')
    print()