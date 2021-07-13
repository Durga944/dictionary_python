dic = {'deepak': 60, 'roshini': 50, 'bijender': 45, 'anjili': 30, 'param': 20}
key=[]
value=[]
for i in dic:
    key.append(i)
    value.append(dic[i])
for j in range(0,len(value)):
    for k in range(0,len(value)):
        if value[j]>value[k]:
            value[j],value[k]=value[k],value[j]
            key[j],key[k]=key[k],key[j]
desending={}
for l in range(0,len(key)):
    desending[key[l]]=value[l]
print(desending)
# {'deepak': 60, 'roshini': 50, 'bijender': 45, 'anjili': 30, 'param': 20}
