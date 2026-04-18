arr = input().split()
while len(arr):
    print(j:=arr.pop(0),end=" ")
    while arr.count(j): arr.remove(j)