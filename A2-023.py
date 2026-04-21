txt = input().upper().replace('I','T')
if txt=="":
    print("nullptr")
    exit()
N , mx , cnt = len(txt) , 0 , 0
if txt.count('T')==N:
    print("unknown",N)
    exit()
if txt[0]=='A':
    print("no 0")
    exit()
for i in range(N-1):
    if txt[i]=='A':
        cnt += 1
        mx = max(cnt,mx)
        continue
    else: cnt = 0
    if txt[i]=='B' and txt[i+1]!='T':
        print("no",i+1)
        exit()
    if txt[i:i+2]=="TA":
        print("no",i+1)
        exit()
    if txt[i]=='R' and txt[i+1]!='A':
        print("no",i+1)
        exit()
if txt[-1] in "BR": print("no",N-1)
else: print("yes",mx)