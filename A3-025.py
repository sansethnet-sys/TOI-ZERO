N , W , L = map(int,input().split())
pt = [[False]*N for i in range(W)]
for i in range(N):
    for j in list(map(int,input().split()))[1:]:
        for p in range(max(j-1-L,0),min(j+L,W)):
            pt[p][i]=True
print(int(any(all(j for j in i) for i in pt)))