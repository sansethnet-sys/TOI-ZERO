txt , mx = input() , 0
tmp , N = txt.upper() , len(txt)
B = tmp.find("B")+1
if 1+tmp.find("BUU") :
    mx =  2
    for i in tmp.split("B") :
        cnt = 0
        for j in i:
            if j!="U" : break
            else : cnt += 1
        mx = max(cnt,mx)
    print("Yes",mx)
elif B : print(txt[:B]+"U"*(N-B))
else : print("BUU"*(N//3)+"BU"[:N%3])