A , B ,C = [input() for i in range(3)]
if len(A)>5 and len(B)>5 : print(A[:2]+B[-1]+C[-1])
else : print(A[0]+C+B[-1])