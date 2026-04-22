CoV = [[],[]]
for tmp in [input() for i in range(int(input()))]:
    if tmp[0]=='1':
        _ , a , b = tmp.split()
        CoV[0].append(b)
        CoV[1].append(a)
    elif tmp[0]=='2':
        print(CoV[0].pop(0),f"({CoV[1].pop(0)})")
    else: print(' '.join(CoV[0]))