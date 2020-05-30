class user():
    def sign_in(self):
        print('logged in')

class wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')

class archer(user):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow
    def check_arrow(self):
        print(f'Arrow remains {self.arrow}')
    def run(self):
        print('ran really fast')

class hybrid(wizard, archer):
    def __init__(self, name, power, arrow):
        archer.__init__(self, name, arrow)
        wizard.__init__(self, name, power)

hybrid1 = hybrid('Borgie', 50, 100)
print(hybrid1.run())
print(hybrid1.check_arrow())
print(hybrid1.attack())
print(hybrid1.sign_in())