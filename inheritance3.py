#Hierarchical Inheritance
class A:
    def aData(self):
        print("class A function called")
class B(A):
    def bData(self):
        print("class B function called")
class C(A):
    def cData(self):
        print("class C function called")
obj=B()              #class b object 
obj1=C()             #class c object 
obj.aData()
obj.bData()
obj1.aData()
obj1.cData()
