class Customer:
    def __init__(self, name, membership_type): # name, membership_type are parameters
        self.name = name
        self.membership_type = membership_type

    def upgrade_membership(self, new_membership):
        self.membership_type = new_membership

    @property
    def get_membership(self):
        return (f"{self.name} is {self.membership_type}")

    #static method - method related to the class, not the instance
    # you call it with Customer.connect_to_db()
    @staticmethod
    def connect_to_db():
        print('connecting to db')

    #MAGIC METHODS
    # custom string representation of an object instance
    def __str__(self):
        return f"{self.name} is {self.membership_type}"

    def __eq__(self, other):
        return self.membership_type == other.membership_type

    __hash__ = None
    __repr__ = __str__ # NICE ONE!!!!

    #############################
    #ENCAPSULATIONS
    # you can hide the inner detail of a class through getters and setters
    # methods that give you access to data

    # getter
    @property
    def name(self):
        return self._name #this is private

    #setter
    @name.setter
    def name(self, new_name):
        self._name = new_name

    #deleter
    @name.deleter
    def name(self):
        del self._name
    ##############################

    ##############################
    #POLYMORPHISM
    # override the method inhereted from the parent class
    ##############################

customers = [Customer("Andreea", "Gold"), Customer("Vlad", "bronze")] # "Andreea", "Vlad" are arguments
print(customers[0].name)

m = Customer("Marian", "Gold")
print(m.get_membership)
m.upgrade_membership("Diamond")
print(m.get_membership)
print(m.name)
Customer.connect_to_db()
print(customers[0] == customers[1])
print(customers)