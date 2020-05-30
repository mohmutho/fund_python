def fib(index):
    a = 1
    b = 0
    for i in range(index):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(10):
    print(x)


'''def fib2(index):
    a = 0
    b = 1
    result = []
    for i in range(index):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2)'''