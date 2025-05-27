import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', 20)
df = sns.load_dataset('titanic')
# print(titanic_data)

# # 산술 연산..
# # 실습 시간에 한 번 각자가 알아서 해보세요.
# df = titanic_data.loc[:, ['age', 'fare']]
# addition_data = df + 10
# titanic_data['mod_age'] = None #age column + 10

# # 1-1. Data 살펴보기
# print(titanic_data.head()) # default: Show 5 lines
# # print(titanic_data.head(10))
# # print(titanic_data.tail())
# titanic_data.info()

# 1-2 데이터 전처리: 범주형 컬럼을 원-핫 인코딩으로 표현
# class_onehot = pd.get_dummies(titanic_data['pclass'])
# class_onehot.columns = ['1st', '2nd', '3rd']
# print(class_onehot.head())
#
# # boolean indexing
# # 나이가 10~20살 사이인 데이터만 가져오기
# df = titanic_data[((titanic_data.age >= 10) & (titanic_data.age <= 20))]
# print(df.head())
# print(len(titanic_data), len(df))
#
# # 나이가 10~20살 이면서 살아있는 사람(survived == 1)
# # 나이가 10~20살 이면서 살아있는 사람(alive == "yes") # ==> survived == alive 같은 내용
# # 조건에 맞는 열을 컬럼 기준으로 슬라이싱 해보자. titanic_data.loc[조건식, pclass: class]
# df = titanic_data.loc[((titanic_data.age >= 10) & (titanic_data.age <= 20))
#                   & (titanic_data.survived == 1), 'pclass': 'class']
# df = titanic_data.loc[((titanic_data.age >= 10) & (titanic_data.age <= 20))
#                   & (titanic_data.survived == 1), ['pclass', 'age', 'class']]
# #
df.info()
df.drop(['age', 'deck', 'class', 'embark_town', 'alive'], axis=1, inplace=True)
# print(df.head())
# embarked의 누락된 행 번호 확인
print(df[df['embarked'].isnull()]) #61, 829
# S, Q, C 중에 제일 빈도가 높은 데이터로 replace (NaN --> Q or C or S)
print(len(df[df['embarked'] == 'S']), len(df[df['embarked'] == 'Q']),
      len(df[df['embarked'] == 'C']))
df.loc[[61, 829], 'embarked'] = 'S'
# print(df[df['embarked'].isnull()]) #61, 829
# print(df.iloc[[61, 829], :])
# df.head()
# df.info()
# 컬럼의 요소가 몇 개로 이루어져있는지 확인 필요.
s = set(list(df['sex']))
w = set(list(df['who']))
print(s, w)
# female:0, male:1, man:0, woman:1, child:2
df['class_sex'] = 0
df['class_who'] = 0

for idx, data in enumerate(df['sex']):
    if data == 'female':
        df.loc[idx, 'class_sex'] = 0
    else: # male
        df.loc[idx, 'class_sex'] = 1

for idx, data in enumerate(df['who']):
    if data == 'man':
        df.loc[idx, 'class_who'] = 0
    elif data == 'woman':
        df.loc[idx, 'class_who'] = 1
    else:
        df.loc[idx, 'class_who'] = 2
print(df.head())

# df_s0 = df[df['sex']=='female']
# df_s0.loc[:, 'sex'] = 0
# df_s1 = df[df['sex']=='male']
# df_s1.loc[:, 'sex'] = 1
# df_s = pd.concat([df_s0, df_s1], axis=0)
# # who 컬럼도 같은 방법으로 한 번 해보세요!!

# class_sex, class_who 사용하고, sex, who 컬럼은 삭제
df.drop(['sex', 'who'], axis=1, inplace=True)

# python ==> lambda, apply...
def bool2int(in_data):
    if in_data == True:
        return 1
    else:
        return 0
df['adult_male_int'] = df['adult_male'].apply(bool2int)
df['alone_int'] = df['alone'].apply(bool2int)
df.drop(['adult_male', 'alone'], axis=1, inplace=True)

onehot_embarked = pd.get_dummies(df['embarked'], prefix='town')
df.drop(['embarked'], axis=1, inplace=True)

df_concat = pd.concat([df, onehot_embarked], axis=1)
print(df_concat)

# Training
x = df_concat.loc[:, 'pclass':'town_S']
y = df_concat['survived']

from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x) # Norm 0~1 사이 값으로.

# dataset train dataset, test dataset 분리
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = (
    train_test_split(x, y, test_size=0.3, random_state=10))
print(f'train data: {x_train.shape}')
print(f'train data: {x_test.shape}')

from sklearn import svm, metrics
# 모델 정의
svm_model = svm.SVC(kernel='rbf')
# train
svm_model.fit(x_train, y_train)

# test data를 가지고 얼마나 잘 맟췄는지 확인
y_hat = svm_model.predict(x_test)
print(y_hat[:10])
print(y_test[:10])

# 학습 모델 성능 평가
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix)

svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)

# accuracy: (TP + TN) / 전체 샘플 수
# ex: precision avg: (0.86 + 0.78) / 2 ==> 단순 평균이므로 데이터 수와는 상관 없음
# weighted precision avg: ((0.86 * 174) + (0.78 * 94)) / (전체샘플 수: 268)