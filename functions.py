#you can make functions so that when its called it would print what is inside the quotations. For example you can call on this by using hello_world()
def hello_world():
    print("hello world")

hello_world()


# add , subtract , multiply , divide ,remainder , exponent
def add(a , b):
    print( a + b)

add(9 , 10)


def subtract(a , b):
    print( a - b)

subtract(9 , 10)


def multiply(a , b):
    print( a * b)

multiply(9 , 10)


def divide(a , b):
    print( a / b)

divide(9 , 10)

def remainder(a , b):
    print( a % b)
remainder(20 , 9)

def exponent(a , b):
    print( a ** b)

exponent(9 , 10)


#Return is  used to return a value to something 
def slope(a, b, c):
    return a * b + c
print(slope(9 , 10 , 16))