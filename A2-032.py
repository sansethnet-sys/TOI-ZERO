n , m = map(int,input().split())
area = [[0]*(m+2) for it in range(n+2)]
pk = []
k = int(input())
for k0 in range(k):
    i , j = map(int,input().split())
    area[i+1][j+1] += 1
mx = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if(area[i][j]): continue
        pk = 0
        for v in range(-1,2):
            for h in range(-1,2):
                pk += area[i+v][j+h]
        if(pk > mx): mx = pk
print(mx)