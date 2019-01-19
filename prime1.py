num=int(input("enter a number "))
i=2
flag=0
while i<num:
    if num%i==0:
        flag=1
        print("no is not prime")
    i+=1
if flag==0:
    print("no is prime")
