A , B , d , r = map(int,input().split())
if A%d>r : A=A//d*d+d
elif A%d<r : A=A//d*d
if B%d>r : B=B//d*d
elif B%d<r : B=B//d*d-d
print(1-(A-B)//d)