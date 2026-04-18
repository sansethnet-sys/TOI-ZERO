txt = input().upper()
dg , N = list(range(2,8)) , len(txt)
f , b = ord(txt[0]) , ord(txt[-1])
for j in range(0,5,2): dg[j]=(f+dg[j])%N%10
for j in range(1,6,2): dg[j]=(b-dg[j])%N%10
print(" ".join(map(str,dg)))