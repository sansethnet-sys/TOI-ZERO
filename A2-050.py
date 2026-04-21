x , j , rs = input() , 1 , []
N , c = int(x[:-1]) , ord(x[-1].upper())
for i in range(N//2+N%2):
    tmp = ['-']*N
    tmp[N-1-i] = tmp[i] = chr(c)
    rs.append(''.join(tmp))
    if c==35: continue
    if c==90: j = -1
    elif c==65: j = 1
    c += j
print('\n'.join(rs[::-1]+rs[N%2:]))