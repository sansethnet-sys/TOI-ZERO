dv = {"BC":[2,3],"CU":[3,4],"UB":[4,4],"BP":[5,5],"PC":[6,6],"UP":[8,7]}
c , n = input()[0:5:4] , int(input())*10
if c not in dv: print("Error")
else: print(dv[c][0]*5+dv[c][1]*n)