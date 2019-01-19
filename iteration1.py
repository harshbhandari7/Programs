#calculating sum by iteration
n=int(input("Enter Number of elements you want to insert in the list "))
list1=[]
for i in range(0,n):
    print("Enter element",i+1,end=' ')
    list1.append(int(input()))

def sum(list1,n):
    sum=0
    for i in range(0,n):
        sum=sum+list1[i]
    print("the sum is ",sum)
sum(list1,n)
