N , K = map(int,input().split())
a1,a2,b1,b2 = [sorted(map(int,[0]+input().split())) for i in range(4)]
mn = 2E9
for i in range(max(K-N,0),min(N,K)+1):
    mx = 0
    for j in range(1,1+i):
        mx = max(a1[j]+b1[i-j+1],mx)
    for j in range(1,K+1-i):
        mx = max(a2[j]+b2[K-i-j+1],mx)
    mn = min(mn,mx)
print(mn)