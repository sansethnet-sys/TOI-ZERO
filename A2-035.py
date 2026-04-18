k , N = 1 , int(input())
A , pt = list(range(N)) , [input() for i in range(N)]
c , cmb = [0]*N , [tuple(A)]
while k < N :
    if c[k] < k :
        if k%2 : A[c[k]] , A[k] = A[k] , A[c[k]]
        else : A[0] , A[k] = A[k] , A[0]
        cmb.append(tuple(A))
        c[k] , k = c[k]+1 , 1
    else : c[k] , k = 0 , k+1
for i in sorted(cmb) :
    for j in i : print(end=pt[j]+" ")
    print()
print(len(cmb))