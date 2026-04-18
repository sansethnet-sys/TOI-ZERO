W , H , N , M = map(int,input().split())
N = list(map(int,[0]+input().split()+[W]))
M = list(map(int,[0]+input().split()+[H]))
tmp = [0]
for i in range(len(N)-1):
    for j in range(len(M)-1):
        tmp = sorted(tmp+[(N[1+i]-N[i])*(M[1+j]-M[j])])[-2:]
print(tmp[1],tmp[0])
