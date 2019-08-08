# Assignment
"""
    =
"""

a = 10
b = a + 10

# Arithmetic
'''
    +
    -
    *
    /
    %
    **
'''
res = a ** 4
print(res)


# Compound assignment

'''
    +=
    -=
    *=
    /=
    %=
    **=
'''

a -= b  # a = a - b

print(a)

# Comparison
'''
    <
    >
    <=
    >=
    ==
    !=
'''

res = a == 10

res = b <= 20

res += a    # res = True + (-10)
print(True + True)


# Logical
'''
    and
    or
    not

    p   q   and or  ~p
    1   1   1   1   0
    1   0   0   1   0
    0   1   0   1   1
    0   0   0   0   1
'''

res = not(a == -10 or b == 20)

print(res)

