#exception handling
try:
    a=int(input("enter a "))
    b=int(input("enter b "))
    c=a/b
    print("c is ",c)
except ZeroDivisionError:
    print("value of b cannot be 0")
    b=int(input("enter value of b other than zero "))
    print("the sum is ",a/b)
