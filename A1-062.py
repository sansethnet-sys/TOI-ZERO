num , cnt = [2]+list(range(3,9975,2)) , 0
for i in range(3,99,2):
    if i in num:
        j = 0
        while i*(i+j)<9975:
            if i*(i+j) in num: num.remove(i*(i+j))
            j += 2
m , n = map(int,input().split())
for it in range(m,1+n):
    cnt += int(it in num)
    if it in num : print(it,end=" ")
print("\nTotal primes:",cnt)