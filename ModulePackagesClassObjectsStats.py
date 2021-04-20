# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:47:11 2020
@author: jw
"""
#%%
#현재 작성하는 코드가 어느 디렉토리에 어느 이름으로 저장되어있는지 확인하는 법
def add_number(n1,n2):
    result=n1+n2
    return result

def gob_number(n1,n2):
    result=n1*n2
    return result

def div_number(n1,n2):
    result=n1/n2
    return result

#%%
#(원래는 위의 함수 저장하고 다른 창에서 실행하기)
import my_cal #my_cal 모듈을 임포트 합니다.
print(my_cal.add_number(1,2)) #my_cal 모듈안에 add_number 함수를 실행해라
print(my_cal.gob_number(1,2)) #2
print(my_cal.div_number(10,2)) #5.0

#%%
#패키지생성하고 모듈이랑 함께 불러오기
from my_loc import my_cal #from 패키지 import 모듈
print(my_cal.add_number(1,2)) #my_cal 모듈안에 있는 add_number함수를 실행해라
#패키지, 모듈이 my_loc(임의로 생성)같은 하나의 폴더 안에 있어야 함

#%%
#파이썬 내장모듈 확인하는 법
import sys
print(sys.builtin_module_names)

#%%
#행렬 출력하기
import numpy as np
a=[[1,2],[4,7]]
a2=np.array(a)
print(a2)

#%%
#Q.다음의 행렬의 합을 출력하시오 [1,2;4,5]+[3,1;6,2]=?
import numpy as np
a=[[1,2],[4,5]]
b=[[3,1],[6,2]]
a2=np.array(a)
b2=np.array(b)
print(a2)
print(b2)
print(a2+b2)
print(a2*b2)

#%%
#Q.다음의 행렬의 합을 출력하시오 a=[[6,3,4],[5,1,7]],b=[[4,5,7],[9,20,4]]
import numpy as np
a=[[6,3,4],[5,1,7]]
b=[[4,5,7],[9,20,4]]
a2=np.array(a)
b2=np.array(b)
print(a2+b2)

#%%
#Q.다음의 행렬의 곱을 구하시오 a=[[1,2],[4,3]], b=[[2,1],[3,4]]
import numpy as np
a=[[1,2],[4,3]]
b=[[2,1],[3,4]]
a2=np.array(a)
b2=np.array(b)
print(np.dot(a2,b2))

#%%
#Q.다음의 행렬의 곱을 구하시오 a=[[3,4,1],[2,4,3]],b=[[2,1],[4,3],[6,7]]
import numpy as np
a=[[3,4,1],[2,4,3]]
b=[[2,1],[4,3],[6,7]]
a2=np.array(a)
b2=np.array(b)
print(np.dot(a2,b2))

#%%
#Q.다음의 리스트에서 최대값을 출력하시오
a=[28,23,21,29,30,40,23,21]
import numpy as np
a2=np.array(a) #np.array로 convert해줘야 np.max등을 쓸 수 있다.
print(np.max(a2))

#%%
#Q.아래의 리스트에서 최대,최소,평균,최빈,중앙값을 출력하시오
a=[28,23,21,29,30,40,23,21]
import numpy as np
from scipy.stats import mode
a2=np.array(a) 
print(np.max(a2))
print(np.min(a2))
print(np.mean(a2)) #평균
print(np.median(a2)) #중앙값
print(mode(a))

#%%
#이미지 파일을 파이썬에서 여는 방법
import PIL.Image as pilimg #이미지를 파이썬에서 시각화 하기위한 모듈
import numpy as np
import matplotlib.pyplot as plt #데이터 시각화 전문 모듈을 임포트합니다.
im=pilimg.open('d:\\data\\lena.png') #lena.png 파일을 읽어서 im에 입력
pix=np.array(im) #넘파이 배열로 변환합니다.
plt.imshow(pix) #화면에 띄웁니다.

#%%
#Q.폐사진을 파이썬에서 시각화하시오
import PIL.Image as pilimg
import numpy as np
import matplotlib.pyplot as plt
im=pilimg.open('d:\\data\\1.png')
pix=np.array(im)
plt.imshow(pix)

#%%
#Q.총을 설계하고 구현해보시오
class Gun(): #클래스 이름은 첫번째 철자는 대문자 나머지는 소문자로 구성한다.
    def charge(self,num): #총알을 장전하는 함수
        self.bullet=num #파이썬 클래스 만들 때 self 키워드는 필수입니다.
    def shoot(self,num): #총을 쏘는 함수
        for i in range(num):
            if self.bullet>0:
                print('탕!')
                self.bullet-=1
            elif self.bullet==0:
                print('총알이 없습니다.')
                break

gun1=Gun() #총 설계도를 이용하여 총을 한개 만들기: gun1이 객체, Gun은 클래스
gun1.charge(10) #gun1이라는 총에 총알 10발 장전하기
gun1.shoot(3)

#%%
#Q.총 설계도를 수정해서 총알을 n발 충전하면 몇발이 충전되었습니다 라는 메세지가 출력되게하시오
class Gun(): 
    def charge(self,num): 
        self.bullet=num
        print(num,'발이 충전되었습니다.')
    def shoot(self,num): 
        for i in range(num):
            if self.bullet>0:
                print('탕!')
                self.bullet-=1
            elif self.bullet==0:
                print('총알이 없습니다.')
                break
        print(self.bullet,'발 남았습니다.')

gun1=Gun() 
gun1.charge(10) 
gun1.shoot(3)

#%%
#Q.총 설계도를 수정해서 총알을 n발 충전하면 몇발이 충전되었습니다 라는 메세지가 출력되게하시오
class Gun(): 
    def __init__(self): #설계도를 가지고 제품을 처음 만들때만 작동되는 함수
        self.bullet=0
        print('총이 만들어졌습니다',self.bullet,'발 장전되었습니다.')
    def charge(self,num): 
        self.bullet=num
        print(num,'발이 충전되었습니다.')
    def shoot(self,num): 
        for i in range(num):
            if self.bullet>0:
                print('탕!')
                self.bullet-=1
            elif self.bullet==0:
                print('총알이 없습니다.')
                break
        print(self.bullet,'발 남았습니다.')

gun1=Gun() 
gun1.charge(10) 
gun1.shoot(3)

#%%
#Q.총 클래스를 이용해서 카드 클래스를 만들고 아래와 같이 카드를 충전하고 사용하시오
class Card(): 
    def __init__(self): #설계도를 가지고 제품을 처음 만들때만 작동되는 함수
        self.money=0
        print('카드가 발급되었습니다',self.money,'원이 충전되었습니다')
    def charge(self,num): 
        self.money=num
        print(num,'원 충전되었습니다.')
    def consume(self,num): 
        if self.money>0:
            self.money-=num
            print(num,'원이 사용되었습니다.')
        elif self.money==0:
            print('잔액이 없습니다')
               
card1=Card() 
card1.charge(10000) 
card1.consume(1000)

#%%
#a라는 리스트 안에 숫자2가 몇개 있는지 세기
a=[1,2,3,1,2,2,2,3,4] #a라는 리스트 객체(제품)가 생성됨
print(a.count(2)) #a리스트에 숫자 2가 몇개있는지 조회

#%%
#Q.초등학생 키에 대한 모집단을 생성하세요
#N=1000000, 평균=140, 표준편차=5
import numpy as np
avg=140
std=5
N=10000000
height=np.random.randn(N)*std+avg
print(height)

#%%
#Q.위 모집단에서 표본을 100개를 추출해서 표본의 평균값을 출력하시오
import numpy as np
avg=140
std=5
N=10000000
height=np.random.randn(N)*std+avg
print(height)
result=np.random.choice(height,100).mean()
print(result)

#%%
#Q.위의 값을 a라는 비어있는 리스트에 담는 작업을 10000번 수행하시오
import numpy as np
a=[]
avg=140
std=5
N=10000000
height=np.random.randn(N)*std+avg
for i in range(1,10001):
    a.append(np.random.choice(height,100).mean())
print(a)

#%%
#Q.위에서 구한 표본평균값들 10000개의 평균값과 표준편차를 s_avg와 s_std변수에 각각 담으시오
import numpy as np
a=[]
avg=140
std=5
N=10000000
height=np.random.randn(N)*std+avg
for i in range(1,10001):
    a.append(np.random.choice(height,100).mean())
    
s_avg=np.mean(a)
s_std=np.std(a)

#%%
#Q.초등학생 키 데이터를 120부터 160까지 0.001 간격으로 생성하시오
import numpy as np
import scipy.stats as norm
a=[]
avg=140
std=5
N=10000000
height=np.random.randn(N)*std+avg
for i in range(1,10001):
    a.append(np.random.choice(height,100).mean())
s_avg=np.mean(a)
s_std=np.std(a)
x=np.arange(120,160,0.001)
print(x)

#%%
#Q.위에서 만든 x키값들을 x축으로 두고 확률밀도함수 그래프를 생성하는데 y축을 구할때
#위에서 구한 평균값, 표준편차를 이용하시오
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import random
a=[]
avg=140
std=5
N=10000000
height=np.random.randn(N)*std+avg
for i in range(1,10001):
    a.append(np.random.choice(height,100).mean())
s_avg=np.mean(a)
s_std=np.std(a)
x=np.arange(138,142,0.001)
y=norm.pdf(x,s_avg,s_std)
plt.plot(x,y,color='blue')
plt.show

#%%
#Q.어느 도시의 초등학생의 수는 전체 10만명입니다. 학생들의 평균키는 140이고 표준편차는 5입니다.
#이 도시의 10만명의 초등학생중 무작위로 한명을 추출했을 때 이 어린이의 키가 145이상 150미만 사이일 확률?
import numpy as np
height=np.random.randn(100000)*5+140
cnt=0
for i in height:
    if i<150 and i>=145:
        cnt+=1
print(cnt/100000)
