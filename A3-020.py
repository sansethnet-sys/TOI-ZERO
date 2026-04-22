H1,H2,B1,B2 = map(int,input().split())
X,Y = map(int,input().split())
N = 0
for I in range(1+min(H1,B1)):
    for J in range(1+min(H2,B2)):
        N = max(N,min(I+J,X)+min(min(H2-J,B1-I)+min(H1-I,B2-J),Y))
print(N)
