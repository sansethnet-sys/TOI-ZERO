c , N , S = map(int,[0]+input().split())
for k in [int(input()) for i in range(N)]:
    if k%4: S-=10*k//3
    else: S-=5*k//2
    if k%12==0: c+=5*k//6
print(S-c,S)