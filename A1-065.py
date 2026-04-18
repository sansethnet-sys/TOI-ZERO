mlc = "#/+*"
arr = list(map(int,input().split()))
for i in arr:
    if i!=0 :
        for j in range(4):
            if i//(10**(3-j)) :
                print(mlc[j],end="")
                i = i%(10**(3-j))
    else: print("-",end="")
