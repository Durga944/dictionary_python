list1=[]
list2=[]
for i in range(0,10):
    name=input("enter any name=")
    marks=int(input("enter any marks="))
    list1.append(name)
    list2.append(marks)
dic={}
for j in range(0,len(list1)):
    dic[list1[j]]=list2[j]
print(dic)