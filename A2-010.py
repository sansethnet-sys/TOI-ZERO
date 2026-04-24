mx , cr = [0]*50005 , [0]*50005
mx[0] , pt , rs = 10**9 , 0 , dict(())
N , K = map(int,input().split())
for i in range(N):
    D , L = map(int,input().split())
    pt += D
    if D==1: cr[pt] = L
    else: cr[pt] += cr[pt+1]+L
    mx[pt] = max(cr[pt],mx[pt])
arr , j = [int(input()) for i in range(K)] , 0
for p in sorted(arr,reverse=True):
    while p<=mx[j]: j += 1
    rs[p] = j-1
for p in arr: print(rs[p])
