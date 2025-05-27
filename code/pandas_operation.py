import pandas as pd

# series + number
student1 = pd.Series({'kor': 100, 'eng': 90, 'math': 92})
# print(student1)
# print(type(student1))

# Normarization
# 각 과목의 점수가 max가 100점 가정
# 점수의 데이터를 0~1사이값으로 변경 # min-max Norm, min-max Scaler
per = student1 / 100 #[100, 100, 100]
# print(per)

# Series +-*/ Series
student2 = pd.Series({'math': 90, 'kor': 70, 'eng': 82})
# print(student1)
# print(student2)

# 사칙연산 결과 출력 해보기
addition = student2 + student1
substraction = student2 - student1
multiplication = student2 * student1
division = student2 / student1
# print(addition)
# print(substrction)

# addition~division <== 각각이 시리즈..
# 사칙연산결과를 데이터프레임으로 만들어보세요.
# index = ['add', 'sub', 'mul', 'div']
df = pd.DataFrame([addition, substraction, multiplication, division], index = ['add', 'sub', 'mul', 'div'])
# print(df)
# print(type(df))
student1 = pd.Series({'kor': 100, 'eng': 90, 'math': 92})
student2 = pd.Series({'kor': 70, 'eng': 82})
sr_add = student1 + student2
sr_sub = student1.sub(student2, fill_value=0)
print(sr_add)
print(sr_sub)

# Series.add/sub/mul/div 메서드 활용해서 fill_value=0 적용 후 각 시리즈의 결과를 데이터프레임으로 변환
# 슬라이드 6페이지(그림1-19 참고) Data frame1 사칙연산 숫자 실습
# 슬라이드 6페이지 Data frame1 사칙연산 Data Frame2 실습