N , P = map(int,input().split())
tl , co = [] , [[0]*N,[0]*N]
for i in range(N):
    tl.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        print(tl[i][j],end=' ')
        if tl[i][j]: co[0][j] += 1
        co[1][j] += tl[i][j]
    print(N-tl[i].count(0),sum(tl[i]))
print(' '.join(map(str,co[0])))
print(' '.join(map(str,co[1])))
print(sum(co[0]),bp:=sum(co[1]),f"{bp*P:.2f}")