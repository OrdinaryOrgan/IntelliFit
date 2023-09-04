## 该代码用于查看维数与能量的关系，以便找到最佳保留维度数

import pandas as pd
from sklearn.decomposition import PCA  
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('./data/combined_keypoints_act1.csv')
X = data.iloc[:, 1:-1]

# PCA分析
pca = PCA()  
pca.fit(X)
explained_variances = pca.explained_variance_ratio_

# 绘制方差解释图
plt.figure()
y = explained_variances.cumsum()
plt.plot(range(1,len(y)+1), y, 'o-')

for i, j in enumerate(y):
    plt.text(i+1, j, str(round(j, 4)))

plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')  
plt.grid()
plt.savefig('variance_act1.png')

# # 根据图形选择合适的维度
# n_components = 10
# # PCA降维
# pca = PCA(n_components=n_components)
# X_pca = pca.fit_transform(X)
# print("PCA dimension: ", X_pca.shape[1])