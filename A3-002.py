N = int(input())
r = int((N-1)**0.5)
print(2*r-(N%2==r%2))