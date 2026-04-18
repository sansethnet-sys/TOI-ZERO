N , C = int(input()) , 0
a = [0]+list(map(int,input().split()))+[0]
for j in range(1,N+1):
    C += a[j-1]<a[j] & a[j]>a[1+j]
print(C)