# Write a function to calculate cube of all the elements from the given list, and calculate the sum of all the elements after calculating the cube.

def calculate_cubes(l):
    res = []
    for ele in l:
        res.append(ele**3)
    return res

def calculate_sum(l):
    sum = 0
    for ele in l:
        sum += ele

    return sum

list1 = [4,2,5,7,2,8,77,26]

print("Given list:", list1)
list2 = calculate_cubes(list1)
print("After calculating cubes:", list2)

print("Sum of all elements:", calculate_sum(list2))
