N , mp , mv = range(int(input())) , input().split() , list(input())
s , t , v = mp.index("1") , mp.index("2") , {"L":-1,"R":1}
while len(mv) and mp.count("2") :
    j = mv.pop(0)
    if s+v[j] not in N : continue
    mp[s] , s , mp[s] = "0" , s+v[j] , "1" 
print(" ".join(mp))