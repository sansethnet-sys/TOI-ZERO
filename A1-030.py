N , pr = int(input()) , list(map(int,input().split()))
for j in range(2*N-2,-1,-2) :
    pr.pop(j + int(pr[j] > pr[j+1]))
if N<1 : print()
elif N==1 : print(pr[0])
else : print(" + ".join(map(str,pr)),"=",sum(pr))
