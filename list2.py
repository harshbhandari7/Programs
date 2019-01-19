#operations on list
#concatenation operator
list1=[10,20,30]
print("list1 is",list1)
list2=[40,50,60]
print("list2 is",list2)
list=list1+list2
print("the combined list is",list)

#concatenation takes place when both the list are of same type.
l1=["h",'a','r']
l2=['s',"h"]
l=l1+l2
print(l)

#MULTIPLIER
l1=[10,20,30]
print("the list is",l1)
n=2
l=l1*n   #this will print the elements 2 times
print("the new list is",l)

#MEMBERSHIP IN,NOT IN

li1=[10,20,30,40]
li2=[10,20]
res=li2 in li1
print(res)
