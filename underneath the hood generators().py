# kayak buat range function sendiri
class mygen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if mygen.current < self.last:
            num = mygen.current
            mygen.current += 1
            return num
        raise StopIteration

gen = mygen(0, 100)
for i in gen:
    print(i)
