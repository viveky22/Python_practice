class employee:
    company = "UST"      #class variable
    def name(self):    #instance method
        print("my name is vivek",self.company)
    @classmethod      #class method
    def lastname(cls):
        print("my last name is yadav",cls.company)
    @staticmethod #static method
    def place():
        print("I'm from uttar pradesh", employee.company)
        
e = employee()
e.name()
e.lastname()
e.place()

