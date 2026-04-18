y = int(input())
print(["yes","no"][bool(y%4 or (y>1581 and not(y%100 and y%400)))])