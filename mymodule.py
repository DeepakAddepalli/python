def square(x):
    return x**2

def cube(x):
    return square(x)*x

def average(*args):
    return sum(args)/len(args)

def get_mobile(**args):
    return args
