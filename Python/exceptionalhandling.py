try:
    a = 5/2
    print(a)
except ZeroDivisionError:
    print("error occured : no cant be divisible by zero")
else:
    print("the no is succesfully devided")
    
finally:
    print("this is our mandatory print, it will execute at last")