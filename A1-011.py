cnt , txt = 1 , input()+"?"
for i in range(len(txt)-1):
    if txt[i]==txt[i+1] : cnt += 1
    else :
        print(cnt,end=txt[i])
        cnt = 1
