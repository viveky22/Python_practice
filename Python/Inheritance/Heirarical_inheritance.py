

class Father:
    def fun1(self):
        print("this is the father class")
class child1(Father):
    def fun2(self):
        print("this is child1 class")

class child2(Father):
    def fun3(self):
        print("this is child2 class")

c1 = child1()
c1.fun1()
c1.fun2()
c2 = child2()
c2.fun1()
c2.fun3()



