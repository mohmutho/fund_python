# set only unique item, not duplicate
my_set = {char for char in 'hello'}
my_set1 = {num for num in range(0,10)}
my_set2 = {num**2 for num in range(0,10)}
my_set4 = {num**2 for num in range(0,10)if num % 2 == 0}

print(my_set4)