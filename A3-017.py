W , L , M , N = map(int,input().split())
print(min([(W%p)*(L%p) for p in range(M,1+N)]))