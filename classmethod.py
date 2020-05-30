class PlayerCharacter :
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    #care about attribute on __init__ class
    #cls, like self, just a parameter yang mengacu ke class
    def adding_thing(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    #don't care  about atribute on __init__ class
    def adding_thing2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Tom', 20)
player2 = PlayerCharacter.adding_thing(4,5)
print(player1.shout())
print(player1.adding_thing(5,4))
print(PlayerCharacter.adding_thing(8,9))
print(player2.age, player2.name)
print(player1.adding_thing2(6,7))