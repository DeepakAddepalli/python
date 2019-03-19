#factorial
i=1;
y=1;
while i<7:
    y =i*y
    i+=1
print(y)
    
def factorial(n):
    f=1
    for x in range(1,n+1):
        f*=x
    return f
print(factorial(6))


#recurrsion

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(3))
print(fact(6))
