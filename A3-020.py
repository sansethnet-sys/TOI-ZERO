H1,H2,B1,B2,N,X,Y = map(int,(input()+" 0 "+input()).split())
for I in range(1+min(H1,B1)):
    for J in range(1+min(H2,B2)):
        N = max(N,min(I+J,X)+min(min(H2-J,B1-I)+min(H1-I,B2-J),Y))
print(N)