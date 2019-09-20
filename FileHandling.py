'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

# f = open("abc.txt", "a")
# f.write(' - The Gurukul for Coders!')


# fp = open("abc.txt", "r")
# data = f.read()

# data = fp.readline()
# print(data)

# data = fp.readline()
# print(data)

# data = fp.readlines()
# print(data)

# print("tell:", fp.tell())

# fp.seek(6, 0)
# name = fp.readline()

# fp.seek(5,1)
# rno = fp.readline()

# fp.seek(7, 1)
# marks = fp.readline()

# print("Name:", name)
# print("Roll no:", rno)
# print("Marks:", marks)

fp = open("xyz.txt", "w")
fp.write(" - The Gurukul for Coders!")