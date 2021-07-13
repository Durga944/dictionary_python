list="MISSISSIPPI" 
dic={}
for i in list:
    count=0
    for j in list:
        if [i]==[j]:
            count+=1
    dic[i]=count
print(dic)