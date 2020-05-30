def generator(num):
    for i in range(num):
        yield i*2

g = generator(100)
print(next(g))
print(next(g))
print(next(g))
print(next(g))