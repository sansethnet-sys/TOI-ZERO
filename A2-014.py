A , B = input().lower() , input().lower()
mx , cnt , Ax , Bx = 0 , 0 , len(A) , len(B)
N , t = max(Ax,Bx) , dict.fromkeys(list("love"),True)
for i in range(max(Ax,Bx)):
    if t.get(A[i%Ax]) or t.get(B[i%Bx]):
        cnt += 1 ; mx = max(cnt,mx)
        print(end='w')
    else:
        N , cnt = N-1 , 0
        print(end='$')
if N%2: print(mx)
elif mx<2 : print('#')