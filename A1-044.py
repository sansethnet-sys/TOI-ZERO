a , d = input().split()
a , p = int(a) , 150
if a < 5: p = 0
elif a < 19: p = 100
if d == "Wed": p //= 2
print(p)
