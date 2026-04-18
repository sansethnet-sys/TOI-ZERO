P , B , D = [int(input()) for i in range(3)]
print(sc:=(P+B)+(D>3)*(P+B)//2)
print(st:=5-(sc<200)-(sc<500)-(sc<1000)-(sc<1500))
if st==5 and D>6: print(99)
else: print(88*(st==4 and B>300))