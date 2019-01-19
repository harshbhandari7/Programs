#Multiple Inheritance
class A:
    def Data(self):                     #Data method in class A
        print("class A Data method")
        
    def aData(self):
        print("class A function called")
class B():
    def Data(self):                   #Method with same name in class B
        print("class B Data method")
    
    def bData(self):
        print("class B function called")
class C(A,B):             # A is inherited first then B      
    def cData(self):
        print("class C function called")
obj=C()
obj.Data()  #that method will be called which is inherited first
obj.aData()
obj.bData()
obj.cData()
