class user():
    def sign_in(self):
        print('logged in')

class wizzard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'Attacking with power of {self.power}')

class archer(user):
    def __init__(self, name, num_arrow):
        self.name = name
        self.num_arrow = num_arrow

    def attack(self):
        print(f'Attacking with power of {self.num_arrow}')

wizzard1 = wizzard('Merlin', 50)
archer1 = archer('Robin', 40)
print(wizzard1.sign_in())
print(archer1.sign_in())
print(wizzard1.attack())
print(archer1.attack())

#polymorphisme = intinya pemanggilan object dengan berbagai cara
#example :
def player_attack(char):
    char.attack()

player_attack(wizzard1)
player_attack(archer1)
