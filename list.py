amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[1])

# List Slicing
amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes']
print(amazon_cart[0::2])

amazon_cart[0] = 'Lemon'
print(amazon_cart)

new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)

new_cart = amazon_cart
new_cart[0] = 'gum'
print(amazon_cart)
print(new_cart)

new_cart = amazon_cart[:]
new_cart[0] = 'gummy'
print(amazon_cart)
print(new_cart)

#adding
basket = [1,2,3,4,5]
new_list = basket.append(6)
print(basket)
print(new_list)

ball = [1,2,3,4,5]
ball.append(6)
new_list1 = ball
print(new_list1)
print(ball)
ball.insert(1, 6)
print(ball)

#removing
print(ball)
ball.pop()
ball.pop(2)
print(ball)
print(ball.pop(1))
ball.clear()
print(ball)
# pop remove tapi return, kalo List.remove() ngga return apa2

ball1 = ['a','b','c','d','e','a']
print('a' in ball1)
print(ball1.index('d'))
print('m' in 'mutho')
print(ball1.count('a'))

# sorting
print(ball1)
new_ball1 = ball1[:]
print(sorted(ball1))
new_ball1.sort()
print(new_ball1)
print(ball1)

#sorrt and reverse
print(ball1)
ball1.sort()
ball1.reverse()
print(ball1)

sentence = ' '.join(['hi', 'my', 'name', 'jojo'])
print(sentence)

coba = list(range(1,10))
a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(*other)
print(d)

# dictionary
dictionary = {'a':[1,2,3],
              'b':'hello',
              'c':True}
my_list = [{'a':[1,2,3],
           'b':'hello',
           'c':True},
           {'a':[4,5,6],
           'b':'holla',
           'c':False}]
print(my_list[1]['a'][1])

dictionary1 = {123:[1,2,3],
              True:'hello',
              'c':True}
print(dictionary1[123])
print(dictionary1[True])
print(dictionary1.get('age'))
print(dictionary1.get('age', 50))
user2 = dict(name = 'Mutho')
print(user2)

user = {
        'name' : 'Mutho',
        'age' : 22,
        'nickname' : 'MM'}
print(22 in user.values())
print('name' in user.keys())
print(user.items())
user2 = user.copy()
user.clear()
print(user)
print(user2)
print(user2.pop('age'))
print(user2)
print(user2.popitem())
user2.update({'nickname' : 'MM',
              'age' : 22})
print(user2)

#tuple seperti list tapi immutable
my_tuple = (1,2,3,4,5,6,6)
print(my_tuple)
print(my_tuple[2])
print(5 in my_tuple)
print(user2['name'])
print(my_tuple.count(3))
print(my_tuple.index(5))

#sets
my_set = {1,2,3,4,5,5}
my_set.add(6)
my_set.add(4)
print(my_set)
my_list1 = [1,2,3,4,5,5,6,6,7,9,8]
print(set(my_list1))
#set not support indexing
print(4 in my_set)
print(list(my_set))
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

#example
set_example = {1,2,3,4,5}
set_example1 = {4,5,6,7,8,9,10}
print(set_example.difference(set_example1))
print(set_example.discard(5))       
set_example
print(set_example.difference_update(set_example1))
set_example
print(set_example.intersection(set_example1))
print(set_example.union(set_example1))
print(set_example.isdisjoint(set_example1))
print(set_example.issubset(set_example1))
print(set_example.issuperset(set_example1))

for item in (1,2,3,4,5,6):
    for x in ['a','b','c']:
        print(item, x)
# iterable - list, dictionary, tuple, set, string
user = {
        'name' : 'Golem',
        'age' : 5006,
        'can_swim' : False}
for item in user.items():
    print(item)
# bisa user.key(), user.value()        
for key, value in user.items():
    print(key)
    print(value)

# counter
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
    print(counter)
for number in range(0, 10, 2):
    print(number)
for i, char in enumerate('Hello'):
    print(i, char)
for i, char in enumerate([1, 2, 3, 4, 5]):
    print(i, char)
for i, char in enumerate(list(range(10))):
    print(i, char)
for i, char in enumerate(list(range(10))):
    if char == 5:
       print('index of 5 is {}'.format(i)) 
x = 0
while x < 10:
    print(x)
    x += 1
else:
    print('done')

mylist = [1, 2, 3, 4]
for item in mylist:
    print(item)

i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1
while True:
    input('Say Something : ')
    break
while True:
    response = input('Hei, Say Something : ')
    if response == 'bye':
        break
mylist = [1, 2, 3, 4]
for item in mylist:
    continue
    print(item)































































