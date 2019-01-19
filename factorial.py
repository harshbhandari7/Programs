# factorial of number using while loop
num=int(input("enter a number "))
i=1
res=num
while i<num:
    res=i*res
    i+=1
print("the factorial of",num,"is",res)    
