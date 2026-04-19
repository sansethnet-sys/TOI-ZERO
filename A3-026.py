gx = {"--":"-","+-":"+","-x":"x","+x":"*"}
N , M = map(int,input().split())
pt = [input() for i in range(2*N)]
for i in range(N):
    print(''.join([gx[pt[i][j]+pt[i+N][j]] for j in range(M)]))