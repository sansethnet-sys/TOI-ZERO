import sys
sys.setrecursionlimit(100002)
N , Mx = int(input()) , 0
pt = {i+1:int(input()) for i in range(N)}
def src(u,v):
    gx , pt[u] = pt[u] , 0
    if gx!=v and gx: return 1+src(gx,v)
    return 1
for i in range(1,1+N): Mx=max(src(i,i),Mx);
print(Mx)