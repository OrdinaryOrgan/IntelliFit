import pandas as pd

df = pd.read_csv('./data/combined_data.csv')

# 读取第一行到一行DataFrame中
first_row = df.iloc[[0]] 

# 从第二行开始读取余下的行到一个新的DataFrame
df = df.iloc[1:]  

# 对df进行随机采样 
df = df.sample(frac=1)

# 将第一行加回到随机采样的DataFrame前面
df = pd.concat([first_row, df]).reset_index(drop=True) 

df.to_csv('./data/shuffled_combined_data.csv', index=False)