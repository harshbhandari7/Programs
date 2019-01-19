#Magic Methods
class Demo:
    "This is a Demo class"
    def demoData(self):
        print("Demo Method")
obj=Demo()
obj.demoData()
#Doc String of class
print("Doc String-",Demo.__doc__)
#Module of class
print("Module of class ",Demo.__module__)
#class related info
print("class Info",Demo.__dict__)
#class name
print("class name",Demo.__name__)
