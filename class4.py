class Employee:
    eno=None
    enm=None
    def setData(self,a,b):
        eno=a
        enm=b
    def getData(self):
        print("employee no is",eno)
        print("employee name is",enm)
eno=101
enm="harsh"
obj=Employee()
obj.setData(eno,enm)
obj.getData()

        
