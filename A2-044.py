demo , rs = "Spider Swamp Arrow Hand Drum".split() , []
demo = [gp+" Demon2" for gp in demo]+["Mugen Train2","Upper Moon3"]
demo[0] , cnt = demo[0].replace('2','1') , 0
demo[2] , pt = demo[2].replace('2','1') , 2
demo[4] = demo[4].replace('2','3')
while len(demo)>2:
    pv , cnt = input() , cnt+1
    if pv==demo[0][-1] or pt==0:
        pt , dx = 2 , demo.pop(0)
        rs += [dx[:-1],"defeat"]
        if pv!=dx[-1]:
            rs[-1] , demo = "escape" , demo+[dx]
    else: pt -= 1
print('\n'.join(rs))
print(cnt)