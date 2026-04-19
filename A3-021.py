N , K = map(int,input().split())
pt = sorted([int(input()) for i in range(N)])
for i in range(1,len(pt)):
    if 1-pt[0]/pt[i]>=1/K : N-=1
print(N)