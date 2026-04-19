arr = sorted([int(input())>18 for i in range(int(input()))])[:-1]
lw = arr.count(0) ; hg = len(arr)-lw ; x = min(lw,hg)
print(1+lw-x+2*hg)