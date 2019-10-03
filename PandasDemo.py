import pandas as pd

stu_data = {'name': ['ABC', 'XYZ', 'PQR', 'LMN'], 'rno': [1, 2, 3, 4], 'marks': [90, 79, 85, 97]}
df = pd.DataFrame(stu_data)

dict1 = {'Python': [20, 40, 25, 63, 54, 34, 34, 67, 89, 23, 45, 78], 'Java': [45, 42, 64, 72, 57, 35, 78, 34, 78, 56, 45, 73], 'C': [34, 54, 23, 67, 23, 34, 56, 53, 36, 89, 45, 34], 'C++': [53, 64, 74, 34, 86, 36, 45, 34, 65, 73, 67, 45], 'Data structures': [45, 45, 56, 56, 34, 45, 56, 23, 78, 78, 67, 23], 'Android': [45, 54, 87, 23, 97, 56, 34, 68, 46, 23, 67, 67], 'iOS': [54, 56, 47, 84, 46, 56, 67, 34, 56, 34, 56, 67]}

df = pd.DataFrame(dict1, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

df1 = pd.DataFrame(dict1, index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

print(df.head())

print(df.tail(3))

print(df.max())

print(type(df[['Python', 'Java']]))

rows, columns = df.shape
print(rows)

print(df.loc['Jan'])

df2 = df.add(df1)

print(df2)


print(df.C[df.C>=40])

print(df[['Python', 'C']][df.C>=40])


df = pd.read_csv('mycsv.csv')

print(df)