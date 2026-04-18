tmp , cnt = input().split()[:-1] , 0
for j in tmp: cnt += int(j[-1])%2
print(cnt,len(tmp)-cnt,len(tmp))