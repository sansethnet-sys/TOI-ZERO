N , S = map(int,input().split())
pt , cnt = [0]+[int(input()) for i in range(N)] , 0
while S!=pt[S] : cnt , pt[S] , S = cnt+1 , S , pt[S]
print(cnt)