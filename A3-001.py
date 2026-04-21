N , pt = int(input()) , [0]
pt += [map(int,input().split()) for i in range(N)]
def dfs(k):
    a , l , b , r = pt[k]
    wl = l if a else dfs(l)
    wr = r if b else dfs(r)
    pt[0] += abs(wl-wr)
    return 2 * max(wl,wr)
dfs(1)
print(pt[0])