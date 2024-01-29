import time
# Dunder -> __ (double underscore)

class Person:
    def __init__(self, name, age): # class constructor
        self.name = name
        self.age = age

    
marian = Person('marian', 45) # call the init method to instanciate the class


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"x: {self.x} | y: {self.y}"

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __call__(self):
        return "i was callled"

    #__repr__ = __str__
    
# v1 = Vector(10,20)
# v2 = Vector(50,60)
# v3 = v1 + v2
# print(len(v3))

#DECORATORS
def mydecorator(func):

    def wrapper():
        print('Im decorating your function')
        func()
        print('I finished decorating your function')
    
    return wrapper

@mydecorator
def hello_world():
    print('Hello world')

# hello_world()

def decorator_with_arg(func):

    def wrapper(*args, **kwargs):
        print('Im decorating your function with arguments')
        return func(*args, **kwargs)
        print('I finished decorating your function with arguments')
    
    return wrapper


@decorator_with_arg
def hello_name(name):
    return(f"Hello {name}")

# print(hello_name('Marian'))

# Practical Example

def logged(func):

    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('logfile.txt', 'a+') as file:
            fname = func.__name__
            file.write(f'{fname} returned value {value}\n')
            print(f'{fname} returned value {value}')
        return value

    return wrapper

@logged
def add(x,y):
    return x + y

# print(add(10,20))

def timed(func):
    def wrapper(*args, **kwargs):
        before = time.time()    #current time
        value = func(*args, **kwargs)
        after = time.time() # current time, after the func run
        fname = func.__name__
        print(f"{fname} took {after - before:02f} seconds to run.")
        return value
    return wrapper

@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

# myfunction(90000)

#GENERATORS
# give you the next value anytime is called
# doesnt store memory, just gives you the result
def mygenerator(n):
    for x in range(n):
        yield x ** 3

# values = mygenerator(900)
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))

# ARGUMENT PARSING
# parsing arguments from the command line
# argparse
# getop

#ENCAPSULATION
# data hidding
# use the setters and getters to control the values
# static method is not related to the object, only tot the class

class Person2:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.isnumeric():
            self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0 and value > self._age:
            self._age = value

    @staticmethod
    def mymethod(age):
        return age > 0

    @property
    def gender(self):
        return "female" if self.name[-1].lower() in "aeiou" else "male"
            

    def __str__(self):
        return f"{self.name} : {self.age}"

# andreea = Person2("Marian", 45)
# print(andreea)
# andreea.age = 36
# print(andreea.gender)

#TYPE HINTING usign mypy - a tool for checking
def my_func(parameter: str) -> str:
    ...

def do_smt(param: list[int]):
    ...

# FACTORY DESIGN PATTERNS

