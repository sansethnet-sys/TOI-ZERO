m , sp = input() , sum([float(input()) for i in range(int(input()))])
if m=="Y": print(f"{0.95*sp:.2f}")
else: print(f"{sp*(1-0.03*(sp>=500)):.2f}")