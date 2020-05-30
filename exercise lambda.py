my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# pengurutan pada key ke 2
b = []
a.sort(key = lambda item: item[1])
b.append(a)
print(a)
print(b)