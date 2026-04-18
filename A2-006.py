tb = [list(input()) for i in range(int(input()))]
def fill(i=len(tb)-1,j=len(tb)-1):
    if i<0 or j<0 : return 0
    if tb[i][j]=="X" : return 0
    tb[i][j] = "X"
    return 1+fill(i-1,j)+fill(i,j-1)
print(fill())