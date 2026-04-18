from math import hypot
pxy = [list(map(int,input().split())) for i in range(int(input()))]
x0 , xn = min(p[0] for p in pxy) , max(p[0] for p in pxy)+1
y0 , yn = min(p[1] for p in pxy) , max(p[1] for p in pxy)+1
for x in range(x0,xn):
    for y in range(y0,yn):
        if all(hypot(x-p[0],y-p[1])==p[2] for p in pxy) :
            print(x,y)
            exit()