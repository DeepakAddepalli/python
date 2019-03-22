def double(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds)
        old_function(*args, **kwds)
    return new_function

def double_in(old_function):
    def new_function(x):
        old_function(2*x)
    return new_function

def add(old_function):
    def new_function(x,y):
        old_function(x+2,y+2)
    return new_function

def sub(old_function):
    def new_function(x,y):
        old_function(x-2,y-2)
    return new_function

@double
def hello():
    print("hello BoA")


@sub
def add(a, b):
    print(a + b)



@double_in
def square(x):
    print(x * x)


hello()
add(3, 4)
square(5)
