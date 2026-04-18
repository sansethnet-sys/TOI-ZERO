N , arr = int(input()) , sorted(map(float,input().split()))
ht , sc = N , 0
for tp in arr: sc , ht = sc+tp , ht-(tp<37)
print(f"SUM={sc:.2f}\nAVG={sc/N:.2f}")
print(f"MEDIAN={(arr[N//2]+arr[(N-1)//2])/2:.2f}")
print(f"MAX={arr[-1]:.2f}\nMIN={arr[0]:.2f}")
print(f"ALERT={ht}")
print("SORTED="+' '.join(list(map(lambda x:f"{x:.2f}",arr))))