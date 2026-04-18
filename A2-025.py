R , C , r0 , c0 = map(int,(input()+" "+input()).split())
tmp , mx = [[0]*C for i in range(R)] , lambda m,n: max(abs(m),abs(n))
for i , j in [map(int,input().split()) for p in range(int(input()))]:
    for r in range(max(0,i-2),min(i+3,R)):
        for c in range(max(0,j-2),min(j+3,C)):
            tmp[r][c] = max(100-40*mx(i-r,j-c),tmp[r][c])
print(sum(i.count(0) for i in tmp))
print(tmp[r0][c0],end='%')