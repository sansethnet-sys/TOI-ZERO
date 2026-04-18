cnt = 0
for i in range(int(input())): 
  cnt += "AEIOU".count(input().upper())
print(cnt)
