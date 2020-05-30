from collections import Counter, defaultdict, OrderedDict
li = [1,2,3,4,5,6,7]
sentence = 'Aku Sayang Kamu Always Love You'
#Counter adalah penghitung item, nanti jadinya berupa dict
print(Counter(li))
print(Counter(sentence))
dictionary = defaultdict(lambda: 'does not exist', {'a':1, 'b':2})
print(dictionary['c'])
#outputnya 'does not exist'
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

d3 = OrderedDict()
d3['b'] = 1
d3['a'] = 2

print(d == d2)
#True
print(d == d3)
#False
