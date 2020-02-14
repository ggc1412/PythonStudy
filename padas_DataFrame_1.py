import pandas as pd
import numpy as np
#dataframe
#보통 데이터 분석, 머신러닝에서 data 변형을 위해 가장 많이 사용
#https://www.kaggle.com/hesh97/titanicdataset-traincsv/data
train_data = pd.read_csv('./train.csv')
##pd.read_csv('./train.csv', sep='구분자') #구분자를 기준으로 구분 설정 가능
##pd.read_csv('./train.csv', header=None) #header를 없는 것으로 지정도 가능
##pd.read_csv('./train.csv', index_col='컬럼명')
#원하는 컬럼을 index로 설정가능 / columns로 조회시 index로 쓰인 column은 안나옴
##pd.read_csv('./train.csv', usecols='PassengerID', 'Survived', 'Name')
#원하는 컬럼만  조회 가능
train_data.head(3)
train_data.tail()
train_data.shape #(891. 12)
print(train_data.describe()) #숫자형 데이터의 기본적인 통계값을 보여줌
print(train_data.info()) #데이터 타입, 메모리 등 기본 정보를 보여줌
##index##
#복잡한 데이터의 경우, 멀티 인덱스로 표현 가능
print(train_data.index)
#RangeIndex(start=0, stop=891, step=1)
#RangeIndex는 처음과 끝 값을 지정함.
print(train_data.columns) #columns값 반환. 다른 데이터 셋 생성 등에 재사용 가능
##dataframe생성하기##
#dictionary에서 생성하기
#dic의 key -> column
data = { 'a' : 100, 'b': [200, 201, 202], 'c' : 300 } #같은 값 혹은 여러 값 지정 가능
dic_data = pd.DataFrame(data, index={'x','y','z'}) #index의 순서가 고정되지 않음
#series에서 생성하기
a = pd.Series([100, 200, 300], ['a','b','c'])
b = pd.Series([101, 201, 301], ['a','b','c'])
c = pd.Series([110, 210, 310], ['a','b','k'])
series_data = pd.DataFrame([a,b,c]) #컬럼명이 다른 경우 NaN으로 들어감.
print(series_data)

##원하는 column의 값만 가져오기
#series_data[0] #KeyError: 0 #dataframe의 경우 []안의 값은 column임
print(train_data['Survived']) #1개의 column 지정시 series 형식으로 반환
print(train_data[['Survived', 'Age', 'Name']]) #원하는 값을 원하는 순서대로 반환 #dataframe 형식

##원하는 row의 값만 가져오기
#기본적으로 []연산자는 column명을 지정하나, slicing만 row레벨로 지원함
print(train_data[7:10])
#row 선택하기
#.loc과 .iloc으로 row 선택 가능
# loc은 인덱스 자체를 사용
train_data.index = np.arange(100,991)
train_data.loc[986]
train_data.loc[[986, 100, 190, 990]]
# iloc은 0 based index 로 사용
train_data.iloc[0:5]
# 둘 다 , 를 사용가능
# loc은 column 선택도 가능
print(train_data.loc[[986, 100, 110, 553], ['Survived', 'Name', 'Age']])
