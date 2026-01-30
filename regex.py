"""."""
import re

rg1 = re.compile(r'\d-(\d\d\d)-(\d\d\d-\d\d\d\d)')  # номер телефона
rg2 = re.compile(r'\d-\d{3}-\d{3}-\d{4}')

s = 'ляляля 8-800-555-3535 ляляля-лололо'
match1 = rg1.search(s)
match2 = rg2.search(s)
print('')
print(match1.group())
print(match2.group())
print(match1.group(1))
print(match1.group(2))
print(match1.groups())
l = ['1']
print(', '.join(l))

def lol():
    return [[2, 5, 6, 0], [4, 7, 1, 3]]
el = lol()
a, b = el[0], el[1]

print(el)
print(a, b)