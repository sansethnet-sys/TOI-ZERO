tm = [0]*1442
n , k = map(int,input().split())
for i in range(n):
    s , t = map(int,input().split())
    tm[s] , tm[t+1] = tm[s]+1 , tm[t+1]-1
for i in range(1440): tm[i+1] += tm[i]
print(' '.join([str(tm[int(i)]) for i in input().split()]))