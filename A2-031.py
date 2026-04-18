gn , k = {"A":"T","C":"G","G":"C","T":"A"} , int(input())
tp = [input().split(),input().split()]
for i in range(int(input())):
    n , p , c = input().split()
    tp[int(n)-1][int(p)] = c
print(' '.join(tp[0])+"\n"+' '.join(tp[1]))
print(sum([gn[c]!=tp[1][i] for i,c in enumerate(tp[0])]))