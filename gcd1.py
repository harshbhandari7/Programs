m=int(input("enter first number "))
n=int(input("enter second number "))
def gcd(m,n):
    i=min(m,n)
    while i>0:
        if (m%i)==0 and (n%i)==0:
            print("greatest common divisor",i)
            break
        else:
            i=i-1
gcd(m,n)
#print(min(45,46,47))
