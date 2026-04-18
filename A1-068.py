N , pt = int(input()) , list(map(int,input().split()))
print(avg:=round(sum(pt)/N,1))
if avg<60 or any(i<50 for i in pt) : print("FAIL")
else : print("PASS")