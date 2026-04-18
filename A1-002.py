N = int(input())
for c in [10,5,2,1]:
    print(c,"=",N//c)
    N %= c