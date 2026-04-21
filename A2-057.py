v = input().replace(' ','')
v = v[v.find('{')+1:v.find('}')]
print(v.replace(',',' -> '))