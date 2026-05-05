class Father:
    def __init__(self):
        print("this is the constructor in father class")
    def fun(self):
        print("this is the father class")

class Child(Father):   #inheritance
    def chil(self):
        #super().__init__()
        super().fun()           #child dont have constructor, so its directly called father constructor
        print("this is the child class")

c = Child()
c.chil()

