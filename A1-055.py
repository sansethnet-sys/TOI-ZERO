P , T = [25,40,55] , list(map(int,input().split()))
cs = sum(P[i]*T[i] for i in range(3))
print(cs*(9+(sum(T)<3))//10)