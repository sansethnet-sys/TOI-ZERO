c = [[0,0],[100,0],[120,0],[200,0],[60,0]]
while c[0][1]==0: c[int(input())%5][1] += 1
print("Bye Bye\nTotal Calories:",sum(i[0]*i[1] for i in c))