# decorator is to change or enhance the function
def my_decorator(func):
    def wrap(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap

@my_decorator
def hello(greeting, emoji =':D'):
    print(greeting, emoji)

hello('Hellooo')
