#calculating sum by recursion
n=int(input("Enter Number of elements you want to insert in the list "))
list1=[]
for i in range(0,n):
    print("Enter element",i+1,end=' ')
    list1.append(int(input()))
def sum(list1,n):
    if n==0:
        return 0
    else:
        return sum(list1,n-1)+list1[n-1]
res=sum(list1,n)
print("The sum is ",res)
