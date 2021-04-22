# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:39:46 2020
@author: jw
"""
#%%
#이스케이프 문자 이해하기
#\ n 줄바꾸기
print('나는 파이썬을 배웁니다. \n파이썬은 자바보다 훨씬 쉽습니다.')
#%%
#리스트 이해하기 []
k=['a','b','c','d','e']
print(k)
print(type(k)) #<class 'list'>
print(k[1]) #b 출력
#%%
#Q.동전의 앞면 뒷면을 10000개 포함한 리스트를 생성하고 10개를 표본추출하시오
import numpy as np
coin=['앞면','뒷면']
coin_10000=coin*10000
sample=np.random.choice(coin_10000,10)
print(sample)
#np.random.choice는 numpy 모듈안에 random코드 안에 choice 함수를 사용하겠다.
#np.random.choice(모집단리스트, 샘플개수)
#%%
#Q.위의 표본추출한 10개 중 앞면이 나오는 횟수를 출력하시오
import numpy as np
coin=['앞면','뒷면']
coin_10000=coin*10000
sample=np.random.choice(coin_10000,10)
print(sample)
cnt=0
for i in sample:
    if i=='앞면':
        cnt+=1
print(cnt)
#%%
#리스트에서 특정요소를 변경하는 방법
a=[1,2,3,4,5]
print(type(a))
print(a[0])
a[0]=7
print(a)
#%%
#Q.a리스트에 인덱스번호 3번째 요소를 17로 변경하시오
a=[1,2,3,4,5]
a[3]=17
print(a)
#%%
#튜플은 데이터를 변경할 수 없습니다.
b=(1,2,3,4,5)
print(b[0])
b[0]=7
#%%
#Q.아래의 숫자 데이터들을 튜플로 생성하고 튜플 변수 이름은 POINT로 하고
#튜플의 모든 요소를 출력하시오
point=(0.01,0.02,0.03,0.04,0.05)
for i in point:
    print(i)
#%%
#사전 이해하기
a = {'apple':'사과', 'banana':'바나나', 'peach':'복숭아', 'pear':'배'}
print(a)
print(type(a))
print(a.keys()) #키값들만 출력
print(a.values()) #값들만 출력
#%%
#사전 이해하기 -2 추가하기
b={}
b['apple']='사과'
b['pear']='배'
b['grape']='포도'
print(b)
#%%
#Q.아래의 두개의 리스트를 각각 만들고 아래와 같이 fruit라는 딕셔너리를 생성하시오
a=['사과','배','포도','복숭아,','바나나']
b=['apple','pear','grape','peach','banana']
fruit={}
for i,k in zip(a,b):
    fruit[i]=k
print(fruit)
#%%
#소문자로 구현하기
a='SCOTT'
print(a.lower())
#or
print('SCOTT'.lower())
#%%
#Q.아래의 문자열을 대문자로 출력하시오
a='scott'
print(a.upper())
print('scott'.upper())
#%%
#Q.다음의 SQL을 파이썬으로 구현하시오
#select lower(ename) from emp;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    print(i.lower())
#%%
#Q.아래의 SQL을 파이썬으로 구현하시오
#select lower(ename), lower(job) from emp;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i,k in zip(emp['ename'],emp['job']):
    print(i.lower(),k.lower())
#%%
#함수 생성하는 법:
def add_number(n1,n2):
    result=n1+n2 #n1에 입력된 값과 n2에 입력된 값을 더해서 result에 입력한다.
    return result #result에 입력된 값을 출력한다.
print(add_number(1,2))

def 함수이름(매개변수1):
실행문
return 출력값이 있는 변수명
#%%
#Q.1부터 10까지 출력하시오
for i in range(1,11):
    print(i)
#%%
#Q. 1부터 10까지 더한 값을 출력하시오
cnt=0
for i in range(1,11):
    cnt=cnt+i
print(cnt)
#%%
#Q.위의 코드를 이용해서 함수를 생성하는데 아래와 같이 숫자를 입력하고 함수를 실행하면
#해당숫자까지 1부터 다 더한 값이 출력되게 하시오 
#print(all_add(10))
def all_add(n1):
    cnt=0
    for i in range(1,n1+1):
        cnt=cnt+i
    return cnt
print(all_add(10))
#%%
#Q.아래의 문자열에서 첫번째 철자만 출력하시오
a='scott'
print(a[0])
#%%
#Q.위에서 출력한 첫번째 철자를 대문자로 출력하시오
a='scott'
print(a[0].upper())
#%%
#Q.아래의 문자열 변수에서 cott만 출력하시오
a='scott'
print(a[1:])
#%%
#Q.첫번째 철자 대문자 나머지는 소문자로 출력되게 하는 함수를 생성하시오
def initcap(val):
    return val[0].upper()+val[1:].lower()
print(initcap('scott'))
#%%
#인자 이해하기
def add_text1(t1,t2):
    return t1+ '  ' + t2
print(add_text1('파이썬','자바')) #파이썬 자바

#매개변수에 아무것도 입력하지 않고 실행하면 기본값이 실행되게하는 함수
def add_text2(t1,t2='최고'):
    return t1+' '+t2
print(add_text2('파이썬'))
#t2에 값을 아무것도 안넣었더니 기본값으로 지정한 최고가 출력되었습니다.
#%%
#전역변수 vs. 지역변수
strdata='전역변수' #func1 함수 외부에 있는 변수(텀블러)
def func1( ):
    strdata2='지역변수' #func1 함수 내부에 있는 변수: 스타벅스 머그컵
    return strdata2
print(func1( ) )
#전역변수 사용
pi=3.141592653589793
def cycle_func1(num1): #원의 넓이를 구하는 함수
    global pi #전역변수 pi를 함수내부로 가져올 수 있습니다. 
			#global 이라는 키워드를 앞에 쓰면 됩니다.
    return pi*num1*num1

def cycle_func2(num1): #원의 1/4인 부채꼴의 넓이를 구하는 함수
    global pi
    return 1/4*pi*num1*num1
print(cycle_func1(5))
print(cycle_func2(5))
#%%
#Q.abs함수를 사용하지 말고 if문을 이용해서 절대값을 출력하는 my_abs함수를 생성하시오
def my_abs(num1):
    if num1<0:
        result=-num1
        return result
    else:
        return num1
print(my_abs(3))
#%%
#time 모듈 연습
import time #time 모듈을 import 합니다.
print('5초간 프로그램을 정지합니다.')
time.sleep(5)
print('5초가 지났습니다.')
#%%
#Q.서울시 초등학생 백만명의 키를 모집단을 구성하는데 평균키가 148.5이고
#표준편차가 30인 모집단을 만들고 100명을 표본으로 추출하여 100명의 평균키를
#비어있는 리스트 a에 입력하는 작업을 10000번 수행하여 a리스트에 10000개의
#표본의 평균키가 입력되게하시오
import numpy as np
from scipy.stats import norm #scipy의stats 패키지로부터 norm이라는 모듈을 import해랴ㅏ
a=[]
avg=148.5
std=30
N=1000000
height=np.random.randn(N)*std+avg
for i in range(1,10001):
    a.append(np.random.choice(height,100).mean())
x=np.arange(140,160,0.001) #140~160까지 0.001간격으로 숫자 생성
y=norm.pdf(x,np.mean(a), np.std(a))
#초등학생 키의 표본평균값들에 대한 확률 밀도함수값이 출력됩니다.
print(y)
#%%
#Q.데이터 시각화 전문 모듈인 matplotlib를 임포트하여 위의 표본평균값 10000개의 데이터에 대한
#확률밀도함수 값으로 정규분포 그래프를 그리시오
import matplotlib.pyplot as plt #matplotlib모듈안에 pylopt라는 함수를 임포트하는데 별칭은 plt
import numpy as np
from scipy.stats import norm 
a=[]
avg=148.5
std=30
N=1000000
height=np.random.randn(N)*std+avg
for i in range(1,10001):
    a.append(np.random.choice(height,100).mean())
x=np.arange(140,160,0.001) 
y=norm.pdf(x,np.mean(a), np.std(a))
plt.plot(x,y,color='blue') #x축은 키, y는 확률밀도함수
plt.show
#%%
#Q.위의 그래프에 색을 더하시오
import matplotlib.pyplot as plt 
import numpy as np
from scipy.stats import norm 
a=[]
avg=148.5
std=30
N=1000000
height=np.random.randn(N)*std+avg
for i in range(1,10001):
    a.append(np.random.choice(height,100).mean())
x=np.arange(140,160,0.001) 
y=norm.pdf(x,np.mean(a), np.std(a))
plt.plot(x,y,color='magenta') 
plt.fill_between(x,y,interpolate=True,color='pink',alpha=0.7) #alpha=투명도
plt.show
