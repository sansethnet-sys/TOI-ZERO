n , gx , pt = int(input())*0 , [] , sorted(map(int,input().split()))
for c in range(400,200,-2) : gx += [c]*9
for c in range(199,-1,-1) : gx += [c+1]*(1+c%2*9)
while len(pt) : n += pt.pop()*gx.pop()
print(n)
