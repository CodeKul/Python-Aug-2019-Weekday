import pandas as pd

df = pd.read_csv('dataset1.csv')
print(df)
print('Shape of df:', df.shape)

df.info(null_counts=True)

# print(df.describe())

print(df.Cost.std())

df.rename(columns = {'Item':'item'}, inplace = True)

print(df)