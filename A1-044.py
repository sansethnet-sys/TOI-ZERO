a , d = input("").split(" ")
p = int(a)
if(int(a)<5): p=0
elif(int(a)<19): p=100
else: p=150
if(d=="Wed"): p//=2
print(p)