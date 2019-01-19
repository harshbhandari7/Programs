#oveloading of function using class
#polymorphism
class Overloading:
    def addData(self,a,*tup):
        for element in tup:
            a=a+element
        print("The sum is ",a)
obj=Overloading()
obj.addData(20,45)
obj.addData(20,45,20,78,74)
obj.addData(1,2,3,4,5)
        
