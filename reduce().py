from functools import reduce
my_list = [1, 2, 3]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

# Iterasi 1 acc = 0, item = 1
# return acc = acc + item = 0 + 1 = 1
# Iterasi 2 acc = 1, item = 2
# return acc = acc + item = 1 + 2 = 3 
# Iterasi 3 acc = 3, item = 3
# return acc = acc + item = 3 + 3 = 6
# selesai iterasi karena listnya sudah habis

print(reduce(accumulator, my_list, 0))
print(my_list)