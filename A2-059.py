n , d = map(int,input().split())
tr = "TechTrends EcoLife FoodieHeaven FashionWeek HealthyLiving".split()
tp , sc , gt = [0]*n , [0]*n , ["STABLE"]*n
for i in range(n):
    tp[i] , x0 , *j , xn = list(map(int,input().split()))
    tp[i] , sc[i] = tr[tp[i]-1] , x0+sum(j)+xn
    if x0<xn : gt[i] = "GROWING"
    if x0>xn : gt[i] = "DECLINING"
for i in range(n):
    print(tp[i]+":",sc[i],"total,",f"{sc[i]/d:.2f}","avg,",gt[i])
print("Top performer:",tp[sc.index(max(sc))])