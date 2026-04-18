N , M = map(int,input().split())
rt = dict({})
for i in range(M):
    S , T = map(int,input().split())
    for j in range(S,T+1):
        if j not in rt: rt[j] = 0
        rt[j] += 1
print(max(rt.values()))