def wish(name,age):
    print("helo {1} your age is {0} years ".format(age,name))
wish("India",70)


def square(x):
    return x**2


print(square(16))
k= square(16)
print(square(square(16)))


#keyword arguments

wish(age= 70, name="india")
