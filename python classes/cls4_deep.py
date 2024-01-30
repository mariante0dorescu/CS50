class Monster:
    def __init__(self, func):
        self.func = func
    
class Attacks:
    def bite(self):
        print("Bite!")

    def strike(self):
        print("Strike!")

    def kick(self):
        print("Kick!")

    def slash(self):
        print("Slash!")

monster = Monster(Attacks().bite())
monster.func