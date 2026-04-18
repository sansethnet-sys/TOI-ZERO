N, C = map(int,input().split())
mt = [list(map(int,input().split())) for i in range(N)]
tp = list(range(1,1+N))
while len(tp)%2==0:
    sb = []
    while len(tp):
        a , b = tp[0]-1 , tp[1]-1
        sb , tp = sb+[mt[a][b]] , tp[2:]
        if a+1!=C and b+1!=C : continue
        if C and sb[-1]!=C: sb[-1] , C = C , 0
    tp = sb
print(tp[0])