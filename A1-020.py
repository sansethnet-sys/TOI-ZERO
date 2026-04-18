a , b , c = [int(input()) for i in range(3)]
if a<b and b<c: print("increasing")
elif a>b and b>c: print("decreasing")
else: print("neither")