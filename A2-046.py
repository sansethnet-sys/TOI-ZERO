for i , pt in enumerate([input().upper() for i in range(int(input()))]):
    v , tx , mx = 0 , 0 , 0
    for c in pt:
        if c in "AEIOU": v , tx = v+1 , tx+1
        else: tx = 0
        mx = max(mx,tx)
    print(f"Line {i+1}: vowels = {v}, max_consecutive =",mx)