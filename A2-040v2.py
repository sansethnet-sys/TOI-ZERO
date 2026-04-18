rn = range(int(input()))
mat = [list(map(int,input().split())) for i in rn]
mat = [[i[j]+int(tr) for j,tr in enumerate(input().split())] for i in mat]
print('\n'.join([' '.join(list(map(str,i))) for i in mat]))