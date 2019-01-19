#program to check whether a 3 digit number is palindrome or not.
num=int(input("enter a number"))
l=num%10
f=num//100
if l==f:
    print("number is palindrome")
else:
    print("number is not a palindrome")
    
