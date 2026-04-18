R , T = input().split() , input().split()
pt = 60+20*("SML".find(R[0])+(R[1]=="T"))
try: print(pt+int(T[1])*(10+5*"EP".find(T[0])))
except: print(pt)