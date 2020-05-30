# lambda expression
# textnya lambda parameter : action(parameter)
from functools import reduce
my_list = [1, 2, 3]

# def multiply_by2(item):
#     return item*2

print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))
print(my_list)
