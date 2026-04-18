for P , C , G in [map(float,input().split()) for i in range(int(input()))]:
    print(end=f"{P+C+G:.1f}")
    if P+C+G>50 : print(end=",Overloaded")
    if P>20 : print(end=",Check Type Plastic")
    if C>20 : print(end=",Check Type Can")
    if G>20 : print(",Check Type Glass")
    else: print()