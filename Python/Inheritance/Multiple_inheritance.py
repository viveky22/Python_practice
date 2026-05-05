class Father:
    def fun1(self):
        print("this is father class")
class Mother:
    def fun2(self):
        print("this is mother class")

class Child(Father,Mother):
    def fun3(self):
        print("this is Child class")

c = Child()
c.fun1()
c.fun2()
c.fun3()