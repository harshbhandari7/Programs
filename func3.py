def func():
    num=int(input("Enter a number "))
    for i in range(2,num):
        if num%i==0:
            print("Number is not prime")
            break
        else:
            print("Number is prime")
            break
func()

def funcc():
    print("function to print prime numbers between 1 and 100")
    for i in range(1,101):
        if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            pass
        else:
            print(i)
funcc()
