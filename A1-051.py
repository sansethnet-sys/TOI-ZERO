c , txt , n = "abcdefghijklmnopqrstuvwxyz" , input() , int(input())
print("".join(c[(n+c.find(j))%26] for j in txt))