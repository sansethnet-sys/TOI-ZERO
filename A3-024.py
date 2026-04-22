cnt , N , L = map(int,[1]+input().split())
vector = [list(map(int, input().split())) for i in range(N)]
for j , k in sorted(vector):
    L = min(L,k)
    if j>L: cnt , L = cnt+1 , k
print(cnt)