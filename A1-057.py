g , k , c = int(input()) , int(input()) , list(range(1,7))
if c.count(g) * c.count(k) :
    if g==k : print("Correct!")
    else : print("Wrong!")
else : print("Invalid")