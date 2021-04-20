# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:26:52 2020
@author: jw
"""
#%%
#문자열에서 특정 문자(열) 위치 찾기 find
txt='A lot of things occur each day'
word_count1=txt.find('o')
print(word_count1) #3이 출력되는데 3은 o라는 철자가 위치하는 인덱스 번호를 리턴합니다.

word_count2=txt.find('day')
print(word_count2) #27

#%%
#Q.우리반 데이터에서 이메일의 @의 위치 인덱스 번호를 출력하시오
import csv
file=open("d:\\data\\emp122.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
for emp_list in emp12_csv:
    print(emp_list[6].find('@'))

#%%
#Q.이메일을 출력하는데 이메일의 첫번쨰 철자부터 세번쨰 철자까지만 출력하시오
import csv
file=open("d:\\data\\emp122.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
for emp_list in emp12_csv:
    print(emp_list[6][:3])
    
#%%
#Q.이메일을 출력하는데 이메일에서 도메인만 출력하시오
import csv
file=open("d:\\data\\emp122.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
for emp_list in emp12_csv:
    add=emp_list[6].find('@') #@의 위치 인덱스번호
    dot=emp_list[6].rfind('.') #.의 위치 인덱스번호인데 뒤에서부터 세기
    print(emp_list[6][add+1:dot])
    
#%%
#문자열을 특정 문자(열)로 분리하기 (split)
a='''1, "김정원", 28, "여", "수학통계학과"''' #양쪽에 싱글'3개 둘러줘야 문자열이 되고 아니면 튜플이되서 split불가
print(a) #(1, '김정원', 28, '여', '수학통계학과')
result=a.split(',') #콤마(,)로 구분해서 리스트에 담는다.
print(result)
       
#%%
#Q.아래의 url 변수에 있는 문자열은 슬래쉬(/)로 구분되어있는데 이 문자열의 요소를
#다음의 리스트처럼 구성하시오
url='http://www.naver.com/news/today=20191204'
print(url.split('/'))

#%%
#문자열을 특정 문자(열)로 결합하기
a=['http:', '', 'www.naver.com', 'news', 'today=20191204']
bond='/'
url=bond.join(a)
print(url)

#%%
#Q.우리반 데이터에서 이름만 출력하시오
import csv
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
for emp_list in emp12_csv:
    print(emp_list[1])
    
#%%
#Q.위에서 출력된 이름을 a라는 비어있는 리스트에 담고 a리스트를 출력하시오
import csv
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
for emp_list in emp12_csv:
    a.append(emp_list[1])
print(a)

#%%
#Q.위의 a리스트에 담겨진 이름을 하나씩 뽑아서 콤마로 연결해서 문자열로 출력되게하시오
import csv
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
for emp_list in emp12_csv:
    a.append(emp_list[1])
bond=','
a.sort() #a 리스트 안의 요소를 ㄱㄴㄷ순으로 정렬합니다. 위치 중요!
result=bond.join(a)
print(result)

#%%
#Q.emp2.csv에서 이름, 월급을 출력하는데 월급을 출력할 때 0 대신 *로 출력하시오
import csv
file=open("d:\\data\\emp22.csv",encoding='UTF8')
emp2_csv=csv.reader(file)
for emp2_list in emp2_csv:
    print(emp2_list[1],emp2_list[5].replace('0','*'))
    
#%%
#Q.아래의 리스트를 name--->홍길동 으로 나오게하시오
a=['name:홍길동', 'age:17', 'major:경영학', 'nation:한국']
for i in a:
    print(i.replace(':','--->'))

#%%
#Q.우리반 데이터에서 이름을 출력하는데 아래와 같이 나이도 같이 출력되게하시오
import csv
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
bond=','
for emp_list in emp12_csv:
    a.append(emp_list[1]+'('+emp_list[2]+')')
    a.sort()
    result2=bond.join(a)
print(result2)
    
#%%
#Q.주사위 2개를 동시에 던져서 두 주사위의 눈의 합이 10이 나오는 확률을 구하시오
import random
dice1=list(range(1,7))
dice2=list(range(1,7))
cnt=0

for i in range (1,10001):
    result1=random.choice(dice1)
    result2=random.choice(dice2)
    if result1+result2==10:
        cnt+=1
print(cnt/10000)

#%%
#Q.아래의 결과를 출력하시오[2,4,6,8,10,12,14,16,18]
a=list(range(2,20,2)) #range(시작숫자, 끝숫자, 스텝). 시작숫자부터 끝숫자 미만까지 스텝만큼 증가해서 출력
print(a)

#%%
#Q.다음의 리스트 b에서 숫자 7을 출력하시오
b=[2,3,4,[5,6],[7,8],9]
print(b[4][0])

#%%
#Q.다음의 리스트 a에서 숫자 4의 인덱스 번호를 출력하시오
a=[1,2,'a','b','c',[4,5,6]]
print(a.index(4)) #4 is not in list
#리스트 안에 있는 리스트의 인덱스 번호는 출력못함

#%%
#Q.list_a의 알파벳 d를 k로 변경하시
list_a=['a','b','c','d','e','f','g']
list_a[list_a.index('d')]='k'
print(list_a)

#%%
#Q.알파벳 a부터 z까지를 담는 리스트를 list_a로 생성하시오
import string #string 모듈안에 알파벳이 들어있습니다.
print(string.ascii_lowercase)
list_a=[]
for i in string.ascii_lowercase:
    list_a.append(i)
print(list_a[:list_a.index('z')])

#%%
#Q.1부터 100까지의 숫자중에 짝수만 아래의 list_a에 담아서 출력하시오
list_a=list(range(2,101,2))
print(list_a)

#%%
#reverse() vs. reversed()
list_a=['a','b','c','d','e']
list_a.reverse() #list_a의 요소 자체를 역순으로 변경한다. (원본데이터를 변경)
print(list_a) #['e','d','c','b','a']
		
list_b=['a','b','c','d','e']
result=reversed(list_b) #list_b의 요소를 역순으로 만들어서 result에 저장
print(list(result)) #['e','d','c','b','a'] 
print(list_b) #=['a','b','c','d','e']

#%%
#Q.다음과 같이 엄마와 아기가 함꼐하는 수영교실 나이 리스트를 생성하시오
listdata1=[34]
listdata2=[2]
listdata3=listdata1*10+listdata2*10
print(listdata3)

#%%
#Q.엄마와 아기가 함께하는 수영교실 나이의 mean, median, mode를 출력하시오
import numpy as np
from scipy import stats
listdata1=[34]
listdata2=[2]
listdata3=listdata1*10+listdata2*10
swim_age=listdata3
print(np.mean(swim_age))
print(np.median(swim_age))
print(stats.mode(swim_age))

#%%
#Q.우리반 나이 데이터를 비어있는 리스트a에 담으시오
import csv
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
for emp_list in emp12_csv:
    a.append(int(emp_list[2]))
print(a)

#%%
#Q.우리반 나이 데이터의 평균값, 중앙값, 최빈값을 출력하시오
import csv
import numpy as np
from scipy import stats
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
for emp_list in emp12_csv:
    a.append(int(emp_list[2]))
np.array(a)
print('평균값:',np.mean(a))
print('중앙값:',np.median(a))
print('최빈값:',stats.mode(a))

#%%
#Q.초등학생 키 데이터로 히스토그램을 그리시오
import numpy as np
import matplotlib.pyplot as plt
height=np.random.randn(100000)*5+150
bins=[142,144,146,148,150,152,154,156,158,160]
hist,bins=np.histogram(height,bins) #결과랑은 상관없고 고수 확인하려고 한번 본 데이터
plt.hist(height,bins,rwidth=0.8,alpha=0.7,color='red') #height:초등학생 10만명 키, bins:도수
#rwidth:히스토그램 그래프의 넓이, alpha: 투명도 
plt.grid() #격자모양이 생김

#%%
#Q.우리반 나이데이터로 히스토그램을 그리시오
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
bins=list(range(24,45,2))
print(bins)
for emp_list in emp12_csv:
    a.append(int(emp_list[2]))
print(a)
plt.hist(a,bins,rwidth=0.7,color='magenta')
plt.grid()
