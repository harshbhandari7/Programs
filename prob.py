N=int(input("Enter the number of potential customers "))
list1=[]
print("Enter the budgets-----")
for i in range(0,N):
    list1.append(int(input("Enter budget of customer"+str(i+1)+" ")))
print(list1)
list1.sort()
print(list1)
if N%2==0:
    i=int(N/2-1)
    price=list1[i]
else:
    i=int(N/2)
    price=list1[i]
print(price)
revenue=0
for i in range(0,N):
    if price<=list1[i]:
        revenue=revenue+price
print("The total revenue is",revenue)
