# Using for loop

# def get_factorial(no):
#     fact = 1
#     for num in range(1, no+1):
#         fact *= num
#     return fact

# Using while loop

# def get_factorial(no):
#     fact = 1
#     while(no > 0):
#         fact *= no
#         no -= 1
#     return fact

# Using recursion

def get_factorial(no):
    if no == 1:
        return no
    return no * get_factorial(no - 1)


no = 23
factorial = get_factorial(no)
print('Factorial of {} is: {}'.format(no, factorial))

