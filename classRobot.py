class Robot:
    '''def __init__(self,name.color,weight):
           self.name=name
           self.color=color
           self.weight=weight'''
         
    def setRobot(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def getRobot(self):
        print("Name is ",self.name)
        print("color is",self.color)
        print("weight is",self.weight)
r1=Robot()
r2=Robot()
r1.setRobot("Tom","Red",30)
r2.setRobot("Jerry","Blue",40)
r1.getRobot()
r2.getRobot()

