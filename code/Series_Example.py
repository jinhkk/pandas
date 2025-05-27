import pandas
import pandas as pd

# dictionary data structure
# val = {'key1':'val1',  'key2':'val2', ....}
# dict_data = {'a': 1, 'b': 2, 'c': 3}
# sr = pd.Series(dict_data)
# print(type(sr))
# print(sr)
# dict_data = {'학번': 20250101, '이름': '홍길동',
#              '생년월일': '1999.01.20'}
# sr = pd.Series(dict_data)
# print(sr)
# test = '1234' / 10
# print(test)

# list_data = ['2025-03-10', 3.14, 'ABC', 100, True]
# sr = pd.Series(list_data)
# print(sr)
# idx = sr.index
# data = sr.values
# print(f'Index Information: {idx}')
# print(data)

# sr = pd.Series([1, 2, 'string'],
#                index=['a', 'b', 'c'])
# sr1 = sr.rename({'a': '1', 'b':'2'})
# sr.rename({'a': 'one', 'b':'two'},
#           inplace=True)
# print(sr1)
# print(sr)

# dict, list ==> Series
# tuple ==> Series ==> index/slicing
tup_data = ('홍길동', '1999-01-01', '남', True)
sr = pd.Series(tup_data, index=['이름', '생년월일',
                                '성별', '학생여부'])
# 데이터 하나 가지고오기
print(sr[0])
print(sr.iloc[0])
print(sr['이름'])
# 데이터를 여러개 가지고 올 수 있음
print(sr[[1, 3]]) # sr[1:4]
# sr['생년월일':'학생여부']
print(sr[['생년월일', '학생여부']])



