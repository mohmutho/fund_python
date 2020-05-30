class user(object):
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('loged in')

class wizard(user):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'The Attack of the {self.name}, is {self.power}, the email is {self.email}')

wizard1 = wizard('Mutho', 100, 'mohammad.mutho@gmail.com')
print(wizard1.email)
print(wizard1.attack())