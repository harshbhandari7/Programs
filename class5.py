enm=None
eno=None
class Employee:
    def __init__(self,a,b):
        enm=a
        eno=b
        print("enm and eno",enm,eno)
    def setData(self,a,b):
        enm=a
        eno=b
        print("setData",enm,eno)
    def getData(self):
        print("Employee name is",enm)
        print("Employee no is",eno)
obj=Employee("Harsh",101)
obj.setData("Jay",102)
obj.getData()

