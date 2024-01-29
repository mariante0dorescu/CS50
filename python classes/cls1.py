class Robot:
    def __init__(self, name:str, color:str, weight:int):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce(self):
        print(f"My name is {self.name}. I have the color {self.color} and my weight is {self.weight}.")


class Person:
    def __init__(self, name:str, personality:str, isSitting:bool):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        # self.robot = robot

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False

r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 40)

r1.introduce()
r2.introduce()

p1 = Person("Alice", "aggresive", False)
p2 = Person("Andreea", "calm", True)

p1.robot_owned = r1
p2.robot_owned = r2

print(p1.robot_owned)
print(p1)