A = [list(map(int,input().split())) for i in range(3)]
B = [list(map(int,input().split())) for i in range(3)]
for i in range(3):
    for j in range(3):
        c = 0
        for k in range(3): c += A[i][k]*B[k][j]
        print(c%32777,end=" ")
    print()