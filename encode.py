bf = input()

def symbol(c):
    return {
        '+': 'Plus',
        '-': 'Minus',
        '>': 'Next',
        '<': 'Prev',
        '.': 'Write',
        ',': 'Read',
        '[': 'OpBrk',
        ']': 'ClBrk',
    }[c]

res = ""
for c in bf:
    res += f"(Cons {symbol(c)} "

res += "Nil"
res += ')' * len(bf)

print(res)

