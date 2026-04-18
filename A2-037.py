em , nm = [] , []
for i in range(int(input())):
    txt = input()
    if txt[0]=="A":
        a , b , c = txt.split()
        if c=="normal": nm.append(b)
        else: em.append(b)
    if txt[0]=="T":
        if len(em): em.pop(0)
        elif len(nm): nm.pop(0)
    if txt[0]=="S":
        if em+nm==[]: print("EMPTY")
        else: print(' '.join(em+nm))