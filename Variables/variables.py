# global and local variables

a = 20      # Global variable
b = 5       # Global variable
d = "Hello" # Global variable

def add():
    c = 10      # local variable
    print(a+b+c)
    print(d)

def sub():
    e = "Python" # local variable
    print(a-b)
    print(d+e)

add()
sub()