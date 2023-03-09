import pandas as pd
import numpy as np


df = pd.read_csv('all_data.csv', index_col=0)
df['id'] = df['id'].astype(int)
df = df.set_index('id')

print(df)
# print(df.index) #index 보여줌
# print(df.columns) #열 보여줌
#print(df.values) #안에 들어있는 numpy 데이터
#df.T #기존 df의 행과 열을 바꾼 형태의 df
# print(df.value_counts('Pay'))
# print(df['CompanyName'].value_counts())

print(df.value_counts("Stacks"))
Stacks_Series = df["Stacks"]
print(Stacks_Series)
for Stacks in Stacks_Series :
    Stacks_List = Stacks.replace("'",'').replace('[','').replace(']','').replace(' ','').split(',')
    print(Stacks_List)

print(df.value_counts("Job"))
print(df['Job'])