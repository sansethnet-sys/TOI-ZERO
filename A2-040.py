n = int(input())
mat = [input().split() for i in range(n)]
for i in range(n):
    arr = input().split()
    for j in range(n):
        mat[i][j]=int(mat[i][j])+int(arr[j])
for i in range(n):
    for j in range(n): print(mat[i][j],end=' ')
    print()
