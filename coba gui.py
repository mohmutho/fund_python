#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show():
    for image in picture :
        for pixel in image :
            if (pixel == 1) :
                print('*', end = ' ')
            else :
                print(' ', end = ' ')
        print(' ')

show()

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

def show_duplicate() :
    duplicate = []
    for value in some_list :
        if some_list.count(value) > 1:
            if value not in duplicate :
                duplicate.append(value)
    print(duplicate)
show_duplicate()

#parameter
#default parameter
def say_hello(name = 'Dek Dia', emoji = ':D') :
    print(f'Hellooo {name}, {emoji}')
#argument
say_hello('Mutho', ':p')
say_hello(emoji = ':p', name ='Nanda')
say_hello()
#return
def sum2(num1, num2):
    return num1 + num2

print(sum2(10, sum(10, 5)))

def sum1(num3, num4):
    def another(n1, n2):
        return n1, n2
    return another(num3, num4)

total = sum1(10, 20)
print(total)

age = input("What is your age?: ")

def checkDriverAge(age = 0):
  if int(age) < 18:
	  print("Sorry, you are too yound to drive this car. Powering off")
  elif int(age) > 18:
	  print("Powering On. Enjoy the ride!");
  elif int(age) == 18:
	  print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(age)

def test(a):
    '''
    Info : this functions test and print param a
    '''
    print(a)
print(test.__doc__)

# cleaning code(jadi lebih ringkas)
def is_even(num) :
    return num % 2 == 0

print(is_even(45))