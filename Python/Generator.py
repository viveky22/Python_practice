def my_generator():
    print("first yeild")
    yield 1
    print("this is my second yield")
    yield 2
    print("this is my third yield")
    yield 3
    print("this is 4th yield")

a = my_generator()
next(a)
print("my name is vivek yadav")
next(a)
next(a)
next(a)