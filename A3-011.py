pv , N , pt  = set([]) , int(input()) , list(map(int,input().split()))
for i in range(N):
    sm = 0
    for j in pt[i:N]: pv , sm = pv|{sm+j} , sm+j
print(len(pv))
