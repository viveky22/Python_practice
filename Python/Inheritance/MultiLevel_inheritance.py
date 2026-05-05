class GrandFather:
    def fun1(self):
        print("this is Grand father class")
class Father(GrandFather):
    def fun2(self):
        print("this is Father class")

class Child(Father):
    def fun3(self):
        print("this is Child class")

c = Child()
c.fun3()
c.fun1()
c.fun2()
