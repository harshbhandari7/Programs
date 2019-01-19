#To add two numbers using class
class Add:
    def addData(self):
        a=int(input("Enter a "))
        b=int(input("enter b "))
        c=a+b
        print("addition of a and b is",c)
        
obj=Add()
obj.addData()
#print(a)  # a is local reference of the function
#this program is not fully object oriented
