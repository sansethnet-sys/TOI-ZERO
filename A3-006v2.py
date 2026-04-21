n , gx , k , pt = int(input())*0 , [0]*402 , 1 , sorted(map(int,input().split()))
for c in range(1,200,2): gx[c] = 1
for c in range(2,201,2): gx[c] = 10
for c in range(202,401,2): gx[c] = 9
while len(pt):
    if gx[k]:
        n += k*pt.pop()
        gx[k] -= 1
    else: k += 1
print(n)