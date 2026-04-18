num = [0,0,1]+([1,0]*16833)
for i in range(3,183,2):
    if num[i]==0: continue
    for j in range(i*i,32768,2*i): num[j] = 0
x = int(input())
print(["No","Yes"][num[x]])
if num[x]: print(' '.join([str(c) for c in range(x+1) if num[c]]))