# if else
'''
if condition:
    true statements
else:
    false statements
'''

a = 20
b = 20

if a < b:
    print('a is less than b')
    print('This is inside if block')
elif a == b:
    print('a and b are equal')
    print('This is inside elif block')
    if a == 30:
        print('a is equal to 30')
    print('Where is this?')
else:
    print('b is less than a')
    print('This is inside else block')

print('This is outside if else')

# Loops

# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')

# while
'''
    initialisation
    while condition:
        statements
        incr/decr
'''

i = 0
while i < 10:
    if i % 2 == 0:
        print('Codekul-',i)
    else:
        print('The Gurukul for Coders!')
    i += 1

'''
    for item in collection:
        statements
'''

for char in ['Codekul', 'Python']:
    print(char)

sum_odd = 0
sum_even = 0
for num in [34,6,24,97, 53, 34,36,22,31]:
    if num % 2 == 1:
        sum_odd += num
    else:
        sum_even += num

print('Sum of odd:', sum_odd)
print("Sum of even:", sum_even)