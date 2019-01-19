class Cons:
    def __init__(self,a,b):
        self.enm=a
        self.eno=b
        print(self.enm,self.eno)
    def __del__(self,a,b):
        print("Destructor invoked")
obj=Cons("Harsh",417)




























        
