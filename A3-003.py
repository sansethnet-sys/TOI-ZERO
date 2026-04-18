N , cnt = int(input()) , 0
P1 , P2 = [list(map(int,[1]+input().split())) for i in range(2)]
def px(a,b,c,d):
    if a>b : a , b = b , a
    if d<c : c , d = d , c
    if a==c and b==d : return 1
    if (a<c and c<b) & (d<a or b<d) : return 1
    return (a<d and d<b) & (c<a or b<c)
for i in range(N):
    cnt += px(P1[i],P1[i+1],P2[i],P2[1+i])
print(cnt)