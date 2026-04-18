txt = list(input().lower())
for v in "aeiou" :
    if txt.count(v) : print(v+":",txt.count(v))