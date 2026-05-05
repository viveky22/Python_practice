def decorator(func):
    def wrap():   #wrapper fucntion
        print("before the function running")
        func()
        print("after the function running")
    return wrap
    
@decorator  #define the decorator, we can give any name in place of decorator as same in function 
def greeting():
    print("Hello vivek yadav")
greeting()
