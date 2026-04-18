N = int(input())
Cs = 5*min(10,N)+7*min(40,max(N-10,0))+10*min(50,max(N-50,0))
Cs += 12*min(100,max(N-100,0))+15*max(N-200,0)
print(f"{Cs*1.07+N/2:.2f}")