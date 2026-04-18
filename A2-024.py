L , P = map(int,input().split())
rc , sc = list(map(int,input().split())) , [0]*3
for i in range(P):
    ps , pt = map(int,input().split())
    for j in range(3): sc[j]+=pt*(ps%rc[j]==0)
mx , kv = max(sc) , ["Rabbit","Monkey","Frog"]
for j,cs in enumerate(sc):
    if cs==mx: print(kv[j],cs)