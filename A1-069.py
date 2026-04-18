N , M = int(input()) , int(input())
A , K = (" A"*M)[1:] , ("K "*M)[:-1]
print('\n'.join([A]*(N//2+N%2)+[K]*(N//2)))