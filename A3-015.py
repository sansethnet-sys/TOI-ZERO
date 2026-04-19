tmp = sorted([int(input()) for i in range(int(input()))])
print(2*sum([tmp[i]*(len(tmp)-i) for i in range(len(tmp))]))