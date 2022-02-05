import re

data = ""
while len(data) == 0 or data[0] != '(':
    data = input()

outputs = map(int, re.sub(r'\(|\)|Cons|Nil', '', data).split())
for x in outputs:
    if x < 128:
        print(chr(x), end='')
    else:
        print(x)
