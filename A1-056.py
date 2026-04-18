from math import hypot as hp
x1,y1,z1 = map(int,input().split())
x2,y2,z2 = map(int,input().split())
print(f"{hp(x2-x1,y2-y1,z2-z1):.2f}")