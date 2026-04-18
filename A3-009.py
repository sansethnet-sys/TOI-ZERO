N , K = map(int,input().split())
pt = [0] * K
for i in range(N): pt[int(input())-1]+=1
print(N-min(pt)*K)