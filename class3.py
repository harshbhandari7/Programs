class Employee:
    eno=None
    enm=None
    def getData(self):
        print("Enter Employee Details:")
        self.eno=int(input("Enter eno"))
        self.enm=input("Enter enm")
    def showData(self):
        print("Employee Details are:")
        print("eno is ",self.eno)
        print("enm is ",self.enm)
obj=Employee()
obj.getData()
obj.showData()
