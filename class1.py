class Demo:
    "This is my first class"
    def getData(self):
        print("It's a Demo class")
obj=Demo()          #Demo() is not a constructor
obj.getData()

print(obj)  #prints object reference location in the memory.


#to get doc string of a class
print("class doc string :",Demo.__doc__)

#to get module of the class
print("class module :",Demo.__module__)

#to get class related information 
print("class info :",Demo.__dict__)      #it returns a dictionary which contains all information about the class

#to get the name of class
print("class name :",Demo.__name__)
        
