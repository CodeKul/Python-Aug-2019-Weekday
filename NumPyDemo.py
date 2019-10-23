import numpy as np

arr = np.array([1,2,3,4,5])

arr = np.array([[1,2,3], [4,5,6]])

print(arr)
print(type(arr))

print(arr[0][1])

arr[1][0] = 40
print(arr)
print(arr.shape)

a = np.zeros((3,3))

a = np.ones((3,3))

a = np.full((3,3), 5.123)

a = np.eye(3)

a = np.random.random((3,3))

a = np.array([[-1, 2, 0, 4], [4, -0.5, 6, 0], [2.6, 0, 7, 8], [3, -7, 4, 2.0]]) 

print(type(a))

print(a[1:3, :1])

print(a[[0, 1, 2, 3], [3, 2, 1, 0]])

print(a[a <= 0])

print(a + 10)
print(a - 10)
print(a * 10)
print(a ** 2)

print(a)
print(a.T)

print(a.max())
print(a.min())
print(a.sum())
print(a.cumsum())

a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[4, 3], 
            [2, 1]]) 
  
# Addition

print(a + b)

print(a - b)

print(a * b)

print(a.dot(b))


arr = np.array([[1, 5, 6], [4, 7, 2], [3, 1, 9]]) 
print(arr.shape)
print(arr.max(axis=0))
print(arr.min(axis=1))

a = np.array([0, np.pi/2, np.pi]) 
print(a)
print ("Sine values of array elements:", np.sin(a)) 


a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 

print ("Square root of array elements:", np.sqrt(a)) 


# Sorting array:

a = np.array([[1, 4, 2], [3, 4, 6], [0, -1, 5]]) 
  
# sorted array 
print ("Array elements in sorted order:\n", np.sort(a, axis = None)) 
  
# sort array row-wise 
print ("Row-wise sorted array:\n", -np.sort(-a, axis = 1)) 
