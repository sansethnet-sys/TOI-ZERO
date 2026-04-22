N , M = map(int,input().split())
r , on = [[] for i in range(N+1)] , [0]*(N+1)
tg , lc , ans , on[1] = [0]*(M+1) , [0]*(M+1) , 1 , 1
for i in range(1,M+1):
    lc[i] , *cur , tg[i] = list(map(int,input().split()))
    for j in cur: r[j].append(i)
def bfs(c=1):
    global ans
    for x in r[c]:
        lc[x] -= 1
        if not (lc[x] or on[tg[x]]):
            on[tg[x]] = 1
            ans += 1
            bfs(tg[x])
bfs()
print(ans)