key=[]
value=[]
for i in dic:
    key.append(i)
    value.append(dic[i])
for j in range(0,len(value)):
    for k in range(0,len(value)):
        if value[j]<value[k]:
            value[j],value[k]=value[k],value[j]
            key[j],key[k]=key[k],key[j]
assending={}
for l in range(0,len(key)):
    assending[key[l]]=value[l]
print(assending)
# {'param': 20, 'anjili': 30, 'bijender': 45, 'roshini': 50, 'deepak': 60}