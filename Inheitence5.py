class A:
    def aData(self):
        print("class a method")

class B(A):
    def bData(self):
        print("class b method")
    def Data(self):
        print("B class Data method")
class C(A):
    def cData(self):
        print("class c method")
    def Data(self):
        print("C class Data method")
class D(B,C):
    def dData(self):
        print("class d method")
obj=D()
obj.Data()
obj.aData()
obj.bData()
obj.cData()
obj.dData()
