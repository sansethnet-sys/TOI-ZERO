import sys
sys.setrecursionlimit(200003)
N , K , T = map(int,input().split())
def cur(x=1+K):
    if x==T or x==1: return 1+(x!=1)
    return 1+cur((x+K)%N)
print(cur())