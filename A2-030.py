arr = [list(map(int,input().split())) for i in range(5)]
rw = ''.join([str(sum(sr)%2) for sr in arr])
cl = ''.join([str(sum(list(sc))%2) for sc in zip(*arr)])
print(rw.find("1"),cl.find("1"))