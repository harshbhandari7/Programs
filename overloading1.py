#constructor overloading
class overloading:
    def __init__(self,a,*tup):
        for element in tup:
            a=a+element
        print("The sum of numbers is",a)
obj=overloading(45,20)
obj=overloading(5,2)

        
