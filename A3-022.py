deg , mx , cn = [False]*360 , 0 , 0
for i in range(int(input())):
    st , fn = map(int,input().split())
    fn += (fn<st)*360
    for j in range(st,fn):
        deg[j%360] = True
for i in range(720):
    cn = (cn+1)*deg[i%360]
    mx = max(cn,mx)
    if mx==360: break
print(mx)