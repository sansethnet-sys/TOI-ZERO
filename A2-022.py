tp = [0]*605
L , N = map(int,input().split())
for i in range(N):
    A , B = map(int,input().split())
    tp[2*A+1] , tp[2*B] = tp[2*A+1]+1 , tp[2*B]-1
for i in range(1,1+2*L): tp[i] += tp[i-1]
print(max(tp[:1+2*L]))