T=int(input("Enter the no of test cases "))
N=int(input("Enter the size of array "))
arr=[]
for i in range(0,N):
    arr.append(int(input("enter element "+str(i)+" ")))
print(arr)
for i in range(0,N):
    swap=False
    for j in range(0,N-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swap=True
    if swap==False:
        break
print("sorted array")
print(arr)
