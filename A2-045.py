A , B = map(int,input().split())
Hs , tf = [] , "XP"
while A * B:
    C , D = map(int,input().split())
    Hs.append(tf[B==C])
    A , B = C , D
while len(Hs): print(str(len(Hs))+Hs.pop())