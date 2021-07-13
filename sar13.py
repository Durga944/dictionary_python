num=int(input("enter any number="))
i=1
list1=[]
list2=[]
while i<=num:
    name=input("enter any name=")
    marks=int(input("enter any marks="))
    list1.append(name)
    list2.append(marks)
    i+=1
j=0
dic={}
while j<len(list1):
    dic[list1[j]]=list2[j]
    j+=1
print(dic)