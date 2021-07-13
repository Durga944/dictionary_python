list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
e={}
i=0
while i<len(list1):
    e[list1[i]]=list2[i]
    i+=1
print(e)
dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# c=0
# for i in dic:
#     if dic[i] in dic:
#         if c==0:
#             c+=1
#             del dic[i]
# print(dic)