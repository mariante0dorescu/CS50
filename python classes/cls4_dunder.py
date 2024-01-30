"""
DUNDER METHODS
__init__ is called when the object is created - MOST IMPORTANT
__len__ is called when the object is passed into len(): len(class_instance)
__abs__ is called when the object is passed into abs(): abs(class_instance)
print(dir(class_instance)) to get all the dunder methods and atributes
__dict__ return the instance as a dictionary
__call__ transforms the instance into a function: monster()
__str__ returns a string represantation of the object
"""
class Monster:
    # constructor
    def __init__(self, health, energy):
        # attributes
        self.health = health
        self.energy = energy

    # dunder
    def __len__(self):
        return self.health
        
    def __abs__(self):
        return self.energy

    def __call__(self):
        print('The monster was called!')

    def __add__(self, other):
        return self.health + other

    def __str__(self):
        return f"This monster has {self.energy} energy"

    # custom methods
    def attack(self):
        print("Attack!!!")
        self.energy -= 10

    def move(self, speed):
        print(f"Move with speed: {speed}")

monster1 = Monster(90,40)
monster2 = Monster(70,70)
# print(monster1.health)   # 90
# print(monster1.energy)   # 40
# monster1.attack()
# print(abs(monster1))   # 90
# print(len(monster1))   # 90
# print(monster1.__dict__)   #{'health': 90, 'energy': 30}
monster1()
print(monster1)