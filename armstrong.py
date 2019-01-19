#To check the entered three digit number is armstrong or not
num=int(input("enter a Number "))
h=num//100
t1=num%100
t=t1//10
o=num%10
num1=h**3+t**3+o**3
if num==num1:
    print("Number is an armstrong")
else:
    print("Number is not an armstrong ")
