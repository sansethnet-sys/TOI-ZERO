a , b , c = input().upper().split()
b , c = map(int,[b,c])
sc , b = "_GBM_".find(a)*500 , 3+(b>4)+(b>9)
sc += ("MGB".find(a)+b)*c*(1+(a=="M"))//100
print((a in "GMB")*sc)