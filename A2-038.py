sc , tp , tx = 0 , [0]*3 , ["\nNO","\nYES"]
for i in range(int(input())):
    bc = list(map(int,input().split()))
    bc = bc[3*(sum(bc[:3])<sum(bc[3:])):]
    for j in range(3): tp[j] , sc = tp[j]+bc[j] , sc+bc[j]
print(sc,"\n"+' '.join(list(map(str,tp)))+tx[tp[0]*2>sc])