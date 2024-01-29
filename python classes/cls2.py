class MyClass:  # "smart data": unit of data with associated functionality (methods)
    '''class that takes name and has a greet function'''

    instance_counter = 0    # class attribute, a variable definded within the class
                            # accesible to all instances (through attribute lookup) 
                            # attribute lookup = python looks for an attribute in the instance, then in the class
                            # MyClass.class_variable    => 0
                            # you can use it inside methods or access it through instances
                            # x.class_variable  => 0


    def __init__(self, name:str):
        self.name = name    # populate, give a value, assign name to attribute in instance
        self.value = 55     # attribute assignment
        MyClass.instance_counter += 1   # increment the class variable
        print('now construction a MyClass instance')


    def greet(self):
        print(f'Hello, {self.name}!\n')   # access the attribute value in instance

    # class method = a method that is designed to work with the class object
    #                rather than the instance object
#                    cls is class instance
    @classmethod
    def get_instance_counter(cls):
        return cls.instance_counter

    # static method = a utility method that belongs in the class
    #                 but doesn't work with the instance or the class
    @staticmethod
    def add(a,b):
        return a + b

class NameAnalyzer:
    def analyze(self):
        #namelen = len(self.name)
        cc = { char: self.name.count(char)
                for char in self.name
                if self.name.count(char) > 1}
        for char in cc:
            print(f"{char}: {cc[char]} occurences")
        return(f'{self.name}: {len(self.name)} characters')

class Person(NameAnalyzer): # inherits the method from NameAnalyzer / parent child relationship
    def __init__(self, name):
        self.name = name


# x = MyClass('Marian')   # encapsulation, set value inside the instance
# y = Person('agamemnon')
# x.greet()               # call the method builtin inside the class, usign the attribute value
# print(x.get_instance_counter()) # 2
# print(y.analyze()) # 2


