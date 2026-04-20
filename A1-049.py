pt , nm = 1 , list(map(int,list(input())[:5]))
if nm[0]>5 : print(end="9")
elif nm[1]>5 : print(end="10")
elif nm[2]>5 : print(end="11")
elif nm[3]>5 : print(end="12")
else : print(13+(nm[4]>5),end="")
if nm==nm[::-1] : 
    if nm[0]+nm[4]>5 : print(end="1")
    else : print(end="02"[nm[1]*nm[3]>5])
elif nm[0]*5<nm[4] : print(end="1")
else : print(end="02"[nm[1]-nm[4]>5])
if sum(nm)>25 : print("1")
else :
    for j in nm : pt *= j
    print("02"[pt>55])