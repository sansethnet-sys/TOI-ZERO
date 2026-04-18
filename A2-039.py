tp , k = [int(input()) for i in range(3)] , int(input())
for i in range(1,4): print("Input number",i,"stored.")
if k==1 :
    print("Original order: "+' '.join(list(map(str,tp))))
if k==2 :
    print("Descending order: "+' '.join(list(map(str,reversed(sorted(tp))))))
if k==3 :
    print("Ascending order: "+' '.join(list(map(str,sorted(tp)))))