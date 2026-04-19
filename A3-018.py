N , K = map(int,input().split())
x = (3*K)**(1/3)-0.5
print(N-int(x-(2*x**3+3*x*x+x-6*K)/(6*x*x+6*x+1)))