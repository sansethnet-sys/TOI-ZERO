N , L = map(int,input().split())
H = [-1]+list(map(int,input().split()))
A = [0]+list(map(int,input().split()))
hx = 0
for i in range(L):
    hx = max(1+max(H[A[i]:A[i+1]]),hx)
    print(abs(min(H[A[1+i]]-hx,0)))