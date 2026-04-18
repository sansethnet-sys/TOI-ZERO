N , tmp = int(input()) , sorted(list(map(int,input().split())))
for i in tmp:
    if tmp.count(i)==1 : print(i,end=" ")
if all(tmp.count(i)!=1 for i in tmp): print(-1)