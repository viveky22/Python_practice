class Payments:   #encapsulation example
    def balance(self, bal):
        self.__bal = bal
        print("this is the balance", self.__bal)
    def get_balance(self):
        return self.__bal
        
    def deposit_b(self,deposit):
        self.deposit = deposit
        self.__bal += deposit
        print("the current blance is ", self.__bal)
        
        
p = Payments()
p.balance(5000)
p.deposit_b(500)
print(p.deposit)
print(p.get_balance())



        