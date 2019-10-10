import pandas as pd

df = pd.read_csv('dataset1.csv')
print(df)
print('Shape of df:', df.shape)

df.info(null_counts=True)

# print(df.describe())

print(df.Cost.std())

df.rename(columns = {'Item':'item', 'Index': 'index', 'Cost':'cost', 'Tax':'tax', 'Total':'total'}, inplace = True)

# df.total = df.cost + df.tax

df.total.fillna(df.cost + df.tax, inplace=True)

df.drop(columns=['index'], inplace=True)

df1 = df[['cost', 'tax', 'total']].corr()

# df.total = df.total.astype(str)

print(df)

print(df.loc[:,['item', 'total']])

# df.cost = 100

f = lambda x : x * 2

df.tax = df.tax.apply(f)

# df = df.sort_values(by='total', ascending=False)

filter = (df.total > 7) & (df.cost < 10)
filtered_df = df[filter]

print(filtered_df)