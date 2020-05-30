class PlayerCharacter:
    #Class Object Atribute
    membership = True
    #constructor
    def __init__(self, name, age):
        if self.membership :
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
    
    def run(self, hello):
        print(f'Cindy {hello}')
        print(f'Umur {self.age}')
        
player1 = PlayerCharacter('cindy', 30)
player2 = PlayerCharacter('Tom', 40)
player2.attack = 50
print(player1.name)
print(player1.age)
print(player1.shout())
print(player1.run('hello'))
print(player2.attack)
