#Method overiding
class Father:
    def show(self):
        print("this is father class")
class Child(Father):
    def show(self):
        super().show()   #to get the father class
        print("this is child class")

c = Child()
c.show()  #method overiding