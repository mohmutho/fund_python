# [parameter for parameter in iterable]
my_list = [char for char in 'hello']
my_list1 = [num for num in range(0, 10)]
my_list3 = [num*2 for num in range(0, 10)]
my_list4 = [num*2 for num in range(0, 10) if num % 2 != 0]
print(my_list4)