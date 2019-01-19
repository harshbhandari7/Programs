#greatest common divisor
n1=int(input("Enter first number "))
n2=int(input("Enter second number "))
list1=[]
list2=[]
for i in range(1,n1+1):
    if n1%i==0:
        list1.append(i)
        
for j in range(1,n2+1):
    if n2%j==0:
        list2.append(j)
#print("divisor",d1)
#print("divisor",d2)
print("Factors of first number",list1)
print("Factors of second number",list2)
#print(list1[len(list1)-1])
list3=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i]==list2[j]:
            list3.append(list1[i])
print("common factors of numbers are",list3)
print("The greatest commom divisor is",list1[len(list3)-1])

