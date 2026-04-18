mn = int(input())
if mn not in range(100,20001) or mn%100 : print("ERROR")
else:
    for i in [1000,500,100]:
        if mn//i : print(i,"=",mn//i)
        mn %= i