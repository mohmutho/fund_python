def super_func(*args):
    print(args)
    print(*args)
    return sum(args)
super_func(1, 2, 3, 4, 5, 6)

def super_func1(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total
print(super_func1(1, 2, 3, 4, 5, 6, num1=15, num2=20, num3= 10))

#Rule : parameter, *args, default parameter, **kwargs

def highest_even(list):
    even = []
    for item in list:
        if item % 2 == 0:
            even.append(item)
    return max(even)

print(highest_even([10, 3, 4, 6, 8, 11]))

total = 0
def count():
    global total
    total += 1
    return total
count()
count()
print(count())

def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inside : ', x)
    inner()
    print('outer : ', x)

outer()
y = 'Hello'[0]
print(y)
