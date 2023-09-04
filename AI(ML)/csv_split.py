import pandas as pd

df = pd.read_csv('./data/shuffled_combined_data.csv') 

# 读取第一行标签到一个单独的DataFrame
tags = df.iloc[[0]]

# 从第二行开始读取数据
df = df.iloc[1:]

# 按照要求进行split
df1 = df.iloc[:len(df)//3]  
df2 = df.iloc[len(df)//3: 2*len(df)//3]
df3 = df.iloc[2*len(df)//3:]

# 分别在各个split DataFrame前加上标签行
df1 = pd.concat([tags, df1]).reset_index(drop=True)
df2 = pd.concat([tags, df2]).reset_index(drop=True)
df3 = pd.concat([tags, df3]).reset_index(drop=True)

df1.to_csv('./data/shuffled_combined_data_split1.csv', index=False)
df2.to_csv('./data/shuffled_combined_data_split2.csv', index=False)
df3.to_csv('./data/shuffled_combined_data_split3.csv', index=False)