N , L = map(int,input().split())
vector = [list(map(int, input().split())) for i in range(N)]
cnt = 1
for j , k in sorted(vector):
    L = min(L,k)
    if j > L: cnt , L = cnt+1 , k
print(cnt)
