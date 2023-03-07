import pandas as pd

df = pd.read_csv('all_data.csv', index_col=0)
df['id'] = df['id'].astype(int)
df = df.set_index('id')

print(df['Stacks'])