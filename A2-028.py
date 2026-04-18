N , f , s = int(input()) , list(input()) , list(input())
f , s , c = list(map(int,f)) , list(map(int,s)) , 0
for j in range(N): c += int(f[j]+s[j]!=9)
if c: print("NO",c)
else: print("YES")