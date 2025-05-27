import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None) # 확인 필요

df = pd.read_csv('../Data/auto-mpg.csv',header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration',
              'model_year', 'origin', 'name']

# # 1. dataframe.head(), tail()
# print(df.head())
# print(df.tail(3))
# print(df.shape)  # 행, 열
# print(df.info())
# print(df.mpg.dtypes)

# # 2. describe()
# # 데이터 프레임의 기술 통계 정보 확인 가능
# print(df.describe()) # 산술 연산이 가능한 컬럼에 대한 정보 반환
# # number, object 모두 보기 위해서는 include='all'
# print(df.describe(include='all'))
# #object, number 형태만 볼 수 있도록 지정 가능
# print(df.describe(include='object'))

# 3. count, value_counts
# value_counts <-- 활용도가 있을 수 있음
# print(df.count())
# uniq_values = df['origin'].value_counts()
# dropna 옵션의 경우에는 count 메서드에는 없음
# uniq_values = df['origin'].value_counts(dropna=True)
# print(uniq_values)

# titanic -> 생존여부별 성별 그룹(카운팅)
# import seaborn as sns
# titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic['deck'].value_counts(dropna=False))
# print(titanic[['survived','sex']].value_counts())

# 성별이 female이고 survived == 0 인 데이터의 갯수는?

# print(titanic[(titanic['survived'] == 0) & (titanic['sex'] == 'female')].count())

# 4. 통계함수

# print(df.mean())
# raise type error ==> object type 데이터는 평균을 구할 수 없음
# df.describe 는 알아서 numeric 컬럼만 가지고 와서 통계 적용

# print(df['mpg'].mean(), df['mpg'].median())
# 두 개 이상 컬럼에 대해서 적용 가능
# print(df[['mpg', 'weight']].mean(), df[['mpg', 'weight']].median())

# To reduce salt-pepper nois using median filter
# 1. 2차원 데이터에서 3x3씩 데이터 가지고 오기
# 2. 가지고온 데이터에서 정렬하기
# 3. 정렬된 배열에서 중간 값(중간에 있는 인덱스의 값 가지고 오기)
# 4. 중간값을 (0,0)부터 넣기.
# 5. 옆으로 한 칸 이동

# 선택정렬 함수 작성(딥러닝 수학 중간 평가)
def select_sort(in_data):
    n = len(in_data)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if in_data[min_idx] > in_data[j]:
                min_idx = j
        in_data[i], in_data[min_idx] = in_data[min_idx], in_data[i]
    return in_data

# test_data = [4, 2, 1, 5, 9]
# print(select_sort(test_data))

# median 함수 작성
def median_filter(img, filter_size):
    filtered_img = img.copy()
    tmp_n = filter_size // 2

    height = len(img)
    width = len(img[0])

    for i in range(tmp_n, height - tmp_n):
        for j in range(tmp_n, width - tmp_n):
            tmp = img[i - tmp_n:i + tmp_n + 1, j - tmp_n:j + tmp_n + 1]
            # 리스트 컴프리헨션 사용해서 1차원 배열로 만들기
            one_d = [item for tmp_list in tmp for item in tmp_list]
            sorted_li = select_sort(one_d)
            mid = sorted_li[len(sorted_li) // 2]
            filtered_img[i][j] = mid

    return filtered_img

import cv2
noise_img = cv2.imread('../Data/saltandpepperlena-300x300.jpg')
in_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2GRAY)
filter_result_img = median_filter(in_img, 3)
# cv2.imshow("filter_result_img", filter_result_img)
# cv2.imshow("orignal", in_img)
# cv2.waitKey()
print(len(in_img), len(in_img[0]))

# print(df.info())
# print(df.max()) # horsepower ==> '?'
# print(ord('?'))
# print(df.horsepower)

# '?' 인 데이터에 해당하는 행을 삭제.
# 데이터 타입을 object ==> float
# 문자열 변경 : replace ('?' ==> NaN)
# NaN drop : df.dropna
# boolean filtering 방식을 이용해서 해보기
# q_df = df[df['horsepower'] == '?'].index
# df.replace({'horsepower' : '?'}, np.nan, inplace=True)
# df.dropna(axis=0, inplace=True)
# df.horsepower = df['horsepower'].astype('float')
# print(df.info())
# print(df['horsepower'].max())
#
# # 표준편차
# print(df.std())
# print(df['mpg'].std())
#
#
# # 상관계수 : 자주 사용함
# # mpg dataset 컬럼에서 object type이 존재하므로 전체에 대한
# # 상관계수를 도출 할 수 없음
# print(df.corr())
print("correlation between mpg and weight")
print(df[['mpg', 'weight']].corr())
print()
print(df[['mpg', 'weight', 'displacement', 'model_year']].corr())


# 4시 이후
# 1. boolean filtering 방식을 이용해서 해보기
# q_df = df[df['horsepower'] == '?'].index
# 2. corr

