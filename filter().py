my_list =  [1,2,3]
def multiply_by2(item):
    return item*2
# intinya filter itu memfilter kalo dia ganjil nambah ke list
# kalo tidak ya ngga nambah
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list)