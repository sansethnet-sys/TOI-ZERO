c , n = input().split()
cl = ["Red","Green","Blue"]
while c!=cl[0][0]:
    cl.append(cl.pop(0))
for j in range(int(n)):
    print(cl[j%3],end=" ")
