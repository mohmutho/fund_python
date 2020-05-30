# map sturcturenya map(function action, yang mau diactionkan)
my_list = [1, 2, 3]
def mutiply_by2(item):
    return item*2

print(list(map(mutiply_by2, my_list)))
print(my_list)
