def my_function():
    print('This is my_function')

my_function()
my_function()

def function_with(param):
    print('Type: ',type(param))
    print('This is my param:', param)

function_with('Codekul')

def function_returning():
    var = 'Codekul'
    return var

str1 = function_returning()
print(str1)

def change_it(my_var):
    print('id1 my_var:',id(my_var))
    my_var = 100
    print('id2 my_var:',id(my_var))
    print('my_var:',my_var)

my_new_var = 10
print('id1 my_new_var:',id(my_new_var))
change_it(my_new_var)
print('id2 my_new_var:',id(my_new_var))
print('my_new_var:',my_new_var)


def change_list(my_list):
    print('id1 my_list:',id(my_list))
    # my_list.append(6)
    my_list = [6,7,8,9,0]
    print('id2 my_list:',id(my_list))
    print('my_list:', my_list)

my_new_list = [1,2,3,4,5]
print('id1 my_new_list:',id(my_new_list))
change_list(my_new_list)
print('id2 my_new_list:',id(my_new_list))
print('my_new_list:',my_new_list)


def function_default(b, a = 10):
    print('a:', a)
    print('b:', b)

function_default(100)


