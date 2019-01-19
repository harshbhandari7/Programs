#Inheritance
class A:
    def aData(self):
        print("class A function called")
class B(A):
    def bData(self):
        print("class B function called")
obj=B()             #class B object created
obj.aData()
obj.bData()

