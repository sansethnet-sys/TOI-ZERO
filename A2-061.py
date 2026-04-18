tm =[[0,"CHE"],[0,"LIV"],[0,"MUN"],[0,"NEW"]]
for i in range(3):
    for j in range(i+1,4):
        h , k = map(int,input().split())
        tm[i][0] += 3*(h>k)+(h==k)
        tm[j][0] += 3*(h<k)+(h==k)
for it,p in enumerate(sorted(tm,key = lambda c:-c[0])):
    print(str(it+1)+". "+p[1],p[0])