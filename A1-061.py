r , x , y = [int(t)**2 for t in input().split()]
if x+y>r: print("OUT")
elif x+y<r: print("IN")
else: print("ON")