# default arguments ex
def foo(a, b=2, c=3):
    print(a,b,c)

foo(1)

def foo1(a, b=4, c=6):
    print(a,b,c)

foo1(4,9)

# unlimited positional arguments and returns tuple
def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1,2,3,4, 5,6,7)

def test(*args):
    print(args)

test(2,4,6,8)

# kwargs - many keyword arguments: return dictionary
def calculate(n, **kwargs):
    print(type(kwargs))  #returns dictionary
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs['add']
    n += kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)

def all_aboard(a, *args, **kwargs):
    print(a, args, kwargs)

all_aboard(4, 7,3,0, x=10, y=20)

class Car:
    def __init__(self, **kwargs):
        # self.make = kwargs['make']    #this will give error if we don't pass an value to solve this we can use get method
        # self.model = kwargs['model']
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')

my_car = Car(make='Honda', model='CR-V', color='black')
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
