bb = {"H":5,"O":3,"J":2}
tt = {"M":[10,15,20],"R":[12,18,25],"T":[15,20,30]}
t , n = input().split()
p , w , v = input().split()
print(bb[t]*int(n)+tt[p][int(w)-1]*int(v))