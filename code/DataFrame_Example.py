import pandas as pd
# dict --> dataframe
# dict_data = {'c0':[1, 2, 3], 'c1': [4, 5, 6],
#              'c2':[7, 8, 9], 'c3':[10, 11, 12]}
# print(type(dict_data))
# df = pd.DataFrame(dict_data)
# print(type(df))
# print(df)
#
# # 행 인덱스/열 이름 지정하여 데이터프레임 만들기
# # 남이, 성별, 거주지역
# df = pd.DataFrame([[23, '남자', '서울'],
#                    [25, '여자', '대구'],
#                    [20, '남자', '부산']],
#                   index=['홍길동', '신수민', '신수아'],
#                   columns=['나이', '성별', '거주지역'])
# print(df)
# print(df.index)
# print(df.columns)
# df.index = ['학생1', '학생2', '학생3']
# df.columns = ['연령', '남녀구분', '지역']
# print(df)
#
# df.rename(index={'학생1':'홍길동', '학생2':'신수민'}, inplace=True)
# df = df.rename(columns={'남녀구분':'남녀'})
# print(df)

# drop

# exam_data = {'인공지능기초': [100, 90, 98], '자료구조': [98, 80, 95],
#              '자바': [100, 100, 80], '기계학습프로그래밍': [100, 100, 100]}
# df = pd.DataFrame(exam_data, index=['std1', 'std2', 'std3'])
# print(df)
# # # label(이름으로 삭제)
# # # df.drop(['std1', 'std2'], inplace=True)
# # # drop using index
# # # df1 = pd.DataFrame(exam_data)
# # # df1.drop([0, 1], inplace=True)
# # df1 = df.drop(['자료구조', '자바'], axis=1)
# # print(df1)
# # df.drop(['std1':'std3'])
#
# # 행 인덱스/이름을 통해 데이터 가져오기
# data = df.loc['std1']
# data1 = df.iloc[0]
# print(type(data))
# print(data)
# print(data1)
# print("===========================")
# data = df.loc[['std1', 'std3']]
# data1 = df.iloc[[0, 2]]
# data2 = df.iloc[0: 3]
# print(type(data))
# print(data)
# print(data1)
# print(data2)
# # 슬라이싱 통해서 데이터를 가지고 올 수 있음
#
# # 컬럼 이름을 통해 데이터 가져오기
# data = df.loc[:,['자바', '자료구조']]  # == df[['자바', '자료구조']]
# print(type(data))
# print(data)
#
# # row, column 사용해서 데이터 가져오기
# data = df.loc[['std1', 'std3'], ['자료구조', '자바']]
# print(data)
#
# ## 50분까지 iloc, loc 활용해서 데이터가져오기 실습...
# data = df.iloc[[0, 1], [1, 2]]
# data = df.iloc[0:2, 1:3]
# data = df.loc['std1': 'std3']
#
# # 교과목: 딥러닝 수학, 자료구조, 웹프로그래밍, 영어, 기계학습, 파이썬기초
# # 학생: 5명 (학생1, 2, .., 5) 인덱스
#
# # 1. 해당 교과목 및 학생에 대한 점수 데이터프레임 생성
# # 2. 자료구조 점수만 가져와서 데이터 타입 확인 및 출력(print(df))
# # 3. 딥러닝수학, 영어, 파이썬 기초 교과목 점수 가져오기 + 데이터 타입 확인
# # 4. 학생1의 영어 점수 가지고 오기 (loc, iloc 둘 다 사용해보기)
# # 5. 학생3의 자료구조, 웹프로그램, 기계학습 점수 가지고 오기 (loc, iloc 둘 다 사용해보기)
# # 6. 학생2의 딥러닝 수학~기계학습 점수 가지고 오기 (슬라이싱 사용)
# # 7. 학생1, 3의 딥러닝 수학~기계학습 점수 가지고 오기
# # 8. 학생2~5에 대한 자료구조, 웹프, 파이썬기초 점수 가지고 오기..
# # 기타..여러 시나리오 만들어서 실습해보세요~~~!!!

exam_data = {'이름': ['학생1', '학생2', '학생3'], '인공지능기초': [100, 90, 98], '자료구조': [98, 80, 95],
             '자바': [100, 100, 80], '기계학습프로그래밍': [100, 100, 100]}
# df = pd.DataFrame(exam_data, index=['std1', 'std2', 'std3'])
# # 새로운 컬럼 추가: 마지막 컬럼에 추가됨
# # df['web_programming'] = 80 # 모든 학생 점수가 80
# df['web_programming'] = [80, 90, 100]
# # 새로운 행 추가: df."loc"
# df.loc['std4'] = 0
# df.loc['std5'] = [90, 100, 80, 90, 96]
# df.loc['std6'] = df.loc['std3']
# # 데이터프레임의 원소값 변경 / Transpose
# df.iloc[3, 0] = 80
# df.iloc[3, [1, 2, 3]] = [90, 100, 100]
# df.iloc[3, 3:] = [90, 100]
# df.loc['std6', :] = [90, 80, 98, 80, 100]
# print(df)
#
# df2 = df.transpose() # df.T
# print(df2)
df = pd.DataFrame(exam_data)
# print(df)
new_df = df.set_index('이름')
# print(new_df)

dict_data = {'c0': [1, 2, 3], 'c1': [5, 4, 6], 'c2': [1, 2, 3], 'c3': [4, 5, 6], 'c4': [4, 5, 6]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
# new_idx = ['r0', 'r1', 'r2', 'r3', 'r4']
# # new_df = df.reindex(new_idx)
# new_df = df.reindex(new_idx, fill_value=0)
# print(new_df)
new_df = df.reset_index()
print(new_df)

new_df = df.sort_index(ascending=False)
print(new_df)

new_df = df.sort_values(by='c1', ascending=False)
print(new_df)