import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern2 = re.compile(r"[A-Za-z0-9$  # %@]{8,}\d")
email = 'mohammad.mutho@gmail.com'
password = 'C4hsmansa1'
check = pattern2.fullmatch(password)
a = pattern.search(email)
b = pattern.findall(email)
c = pattern.fullmatch(email)
#dia pencrian difullkan match ngga sepenuhnya
d = pattern.match(email)
print(check)
print(a.span())
print(a.start())
print(a.group())
print(a.end())
