N , rs = int(input()) , 0
arr = [list(map(int,input().split())) for i in range(N)]
A , B = sorted([X+Y for X,Y in arr]) , sorted([X-Y for X,Y in arr])
for i in range(N): rs += abs(A[i]-A[N//2])+abs(B[i]-B[N//2])
print(rs)