# str 
str1 = "Codekul"
print(str1)
print(type(str1))

str2 = 'Codekul'
print(str2)
print(type(str2))

#Codekul - The gurukul for coders! 

str3 = '"Codekul - The gurukul for coders"'
print(str3)

a = 10
b = 20

str4 = "Addition of {} & {} : {}".format(a,b,a + b)

print(str4)

print("Addition of %d and %d is %d"%(a,b,a+b))


# List

list1 = [1,2,3,4,5,'Six',9.9,True]

list1.insert(1,100)

print(list1)
print(list1[7])

list1.append('Ten')
list1.reverse()
print(list1)

list2 = ["One","Two"]
list3 = list1 + list2 

print(list3)
#list3.sort()

# Dictionary

dict1 = {'key1': 'value1', 'key2' : 'value3', 'key3':3}

print(dict1['key1'])

dict2 = {1:'One',2:'Two', 3:'Three','Five':5}

print(dict2[2])

# Tuple

tup1 = (1,2,3,4,5)
print(tup1[2])

#tup1.append(10)  - Cant append in tuple
l1 = [4,5,7,4,51,3]
print(sorted(l1, reverse = False))



