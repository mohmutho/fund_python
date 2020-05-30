# High Order Function seperti dibawah
def greet(func):
    func()
# bentuk lainnya seperti dibawah
def greet2():
    def func():
        return 5
    return func