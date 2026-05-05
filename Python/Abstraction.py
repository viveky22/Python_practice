from abc import ABC, abstractmethod
class Payments(ABC):
    def set_bal(self,amount):
        self.amount = amount
        
    @abstractmethod                          #Abstraction → hides how it works
    def Pay(self, amount):                   #Encapsulation → hides data (variables)
        pass
class UPI(Payments):
    def Pay(self,upi):
        self.amount += upi
        print(f"the amount paid by UPI is {upi} and reminaing balance is {self.amount}")
class Creditcard(Payments):
    def Pay(self, creditcard):
        self.creditcard = creditcard
        self.amount += creditcard
        print(f"the amount paid by credit card is {creditcard} and remaing balance is {self.amount}")
        


b = UPI()
b.set_bal(10000)
b.Pay(5000)
c = Creditcard()
c.set_bal(3000)
c.Pay(2000)
