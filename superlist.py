class superlist(list):
    def __len__(self):
        return 1000

superlist1 = superlist()

print(len(superlist1))
superlist1.append(5)
print(superlist1[0])
print(issubclass(superlist, list))