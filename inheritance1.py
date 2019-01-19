#Multilevel Inheritance
class A:
    def aData(self):
        print("class A function called")
class B(A):
    def bData(self):
        print("class B function called")
class C(B):
    def cData(self):
        print("class C function called")
obj=C()             #class c object created
obj.aData()
obj.bData()
obj.cData()
