import pandas as pd
import matplotlib.pyplot as plt
from plotly import matplotlylib

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
# encoding cp949 해야됨 이유 모름 걍 하셈
# index 가 매장이 되어야함
df = pd.read_csv('../Data/sell_bike.csv', index_col='자전거매장',
                 encoding='cp949')
# print(df.head())
# df.plot(kind='bar') # 컬럼 : 라벨(범례), index : x축, 값 : y축
# plt(matplotlylib)
# plt(index, value)
# plt.show()

index = [1, 2, 3, 4, 5, 6]
London = list(df.loc['런던'].values)
York = list(df.loc['요크'].values)
l_450 = []
for val in London:
    if val >= 450 : l_450.append(val)
    else:l_450.append(0)
y_450 = [val if val >= 450 else 0 for val in York]

plt.subplot(2, 1, 1)
plt.bar(index, London, color='red')
plt.bar(index, l_450, color='orange')
plt.subplot(2, 1, 2)
plt.bar(index, York, color='red')
plt.bar(index, y_450, color='orange')

plt.show()
# print(London)