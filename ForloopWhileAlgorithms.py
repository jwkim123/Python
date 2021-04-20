# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:51:40 2020
@author: stu23
"""
#%%
#for loop문을 이용해서 구구단 2단 출력하기
for i in range (1,10): #1부터 9까지 반복하겠다
    print('2 x ',i,'=',2*i)
#%%
#구구단 전체 출력
for i in range (2,10):
    for j in range (1,10): #중첩 loop 문
        print(i,'*',j,'=',i*j)
#%%
#주사위를 10번 던져서 주사위의 눈을 10개 출력하시오
import random
dice = [1,2,3,4,5,6]
for i in range (1,11):
    print (random.choice(dice))
#%%
#주사위를 10번 던졌을 때 짝수가 나오는 횟수를 출력하시오
import random
dice = [1,2,3,4,5,6]
cnt=0
for i in range (1,11):
    result = random.choice(dice) #주사위의 눈이 result 변수에 할당된다
    if result%2==0: #result 변수의 주사위의 눈이 짝수이면
        cnt=cnt+1 #cnt를 1씩 증가 시킨다
print(cnt) #print의 위치를 for 문과 맞춰줘서 cnt에 담긴 최종 결과를 출력한다.
#%%
#
import random
dice = [1,2,3,4,5,6]
for j in range(1,6):
    cnt=0
    for i in range (1,11):
        result = random.choice(dice)
        if result%2==0:
            cnt=cnt+1 
    print(cnt) 
#%%
#동전을 100번 던져서 앞면이 나올 확률을 출력하시오
import random
coin = ['앞면','뒷면']
cnt=0
for i in range (1,101):
    result = random.choice(coin)
    if result == '앞면':
        cnt=cnt+1
print(cnt/100)
#%%
#위의 작업을 50번 반복해서 확률을 50개 출력하시오
import random
coin = ['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range (1,101):
        result = random.choice(coin)
        if result == '앞면':
            cnt=cnt+1
    print(cnt/100)
#%%
#리스트 append 함수
a=[]
a.append(7) #a 리스트에 숫자 7을 넣는다
print(a)
a.append(8) #a 리스트에 숫자 8을 넣는다.
print(a)
#%%
#50번 반복한 확률을 append에 넣으시오
a=[] #비어있는 리스트 a를 생성한다.
import random
coin = ['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range (1,101):
        result = random.choice(coin)
        if result == '앞면':
            cnt=cnt+1
    print(cnt/100)
    a.append(cnt/100) #a리스트에 확률을 입력한다.
print(a)
#%%
#두개의 동전을 동시에 300번 던져서 둘 다 앞면이 나오는 횟수를 출력하시오
import random
coin1 = ['앞면','뒷면']
coin2 = ['앞면','뒷면']
cnt=0
for i in range (1,301):
    result1 = random.choice(coin1)
    result2 = random.choice(coin2)
    if result1=='앞면' and result2=='앞면':
        cnt=cnt+1
print(cnt)
#%%
#x라는 리스트를 만들고 x라는 리스트에 위의 문제에서 앞면이 나오는 횟수를 x리스트에 담는데
#둘 다 앞면이 나오는 횟수를 출력하는 forloop 문을 1000번 반복해서 x리스트에 입력하시오
import random
x=[]
coin1 = ['앞면','뒷면']
coin2 = ['앞면','뒷면']
for j in range(1,1001):
    cnt=0
    for i in range (1,301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if result1=='앞면' and result2=='앞면':
            cnt=cnt+1
    x.append(cnt)
print(x)
#%%
#두개의 동전을 300번 던져서 둘 다 앞면이 나오는 횟수를 확률변수 X라고 할 때, X의 
#평균과 분산 및 표준편차를 구하라
import random
import numpy as np #넘파이 모듈을 이 코드에서 사용
x=[]
coin1 = ['앞면','뒷면']
coin2 = ['앞면','뒷면']
for j in range(1,1001):
    cnt=0
    for i in range (1,301):
        result1 = random.choice(coin1)
        result2 = random.choice(coin2)
        if result1=='앞면' and result2=='앞면':
            cnt=cnt+1
    x.append(cnt)
print(np.mean(x))
print(np.var(x))
print(np.std(x))

#%%
#한개의 주사위를 360번 던져서 3의 배수의 눈이 나오는 횟수를 X라고 하고  
#1000번 반복했을 때 이 X의 평균, 분산, 표준편차를 출력하시오
import random
import numpy as np
x=[]
dice = [1,2,3,4,5,6]
for j in range(1,1001): #1000번 반복수행하는 for loop 문 작성
    cnt=0 #cnt에 0 할당
    for i in range (1,361): #360번 반복수행하는 for loop 문 작성
        result = random.choice(dice) #주사위에서 눈을 하나 출력해서 result에 담는다.
        if result%3==0: #그 주사위의 눈을 3으로 나눈 나머지 값이 0이면
            cnt=cnt+1 #cnt를 1씩 증가시키겠다.
    x.append(cnt) 
print(np.mean(x))
print(np.var(x))
print(np.std(x))
#%%
#for 문 개념 배우기 (for~continue~break)
for 변수 in 범위:
    실행코드
continue  #이 부분은 그냥 지나치고 다음 반복문을 수행해라
    실행코드
break #for 반복문 end
#%%
#5를 제외하고 1에서 10까지 출력하시오
for i in range(1,11):
    if i == 5:
        continue #for 아래, continue 윗부분은 그냥 지나치고 다음 루프문을 실행해라
    print(i)
#%%
#1부터 10까지 짝수만 출력하시오
for i in range(1,11):
    if i%2==1:
        continue
    print(i)
#%%
#1부터 10까지의 합을 구하시오
cnt=0
for i in range(1,11):
    cnt=cnt+i
print(cnt)
#or
x=[]
for i in range(1,11):
    x.append(i)
print(sum(x))
#%%
#for문에서 사용하는 break: 루프문을 중단시키는 역할을 하는 키워드
for i in range(1,11):
    print(i) #i를 출력하다가
    if i==3: #i가 3을 만나면
        break #루프문 종료
#%%
#1부터 100번까지 출력하는 forloop문을 작성하는데 숫자를 물어보게해서 입력된숫자
#까지만 출력하시오
a=int(input('숫자를 입력하세요'))
for i in range(1,100):
    print(i)
    if i==a:
        break
#%%
#최대공약수를 출력하시오
x=[]
a=int(input('숫자1을 입력하세요'))
b=int(input('숫자2를 입력하세요'))
for i in range(1,11):
    if a%i==0 and b%i==0:
        break
print(a,'와',b,'의 최대공약수는 ',i,'입니다')
#%%
#
a=int(input('숫자를 입력하세요'))
for i in range(1,1+a):
    print(i)
else:
    print('perfect')
#%%
#
a=int(input('숫자를 입력하세요'))
b=int(input('중단할 숫자를 입력하세요'))
for i in range(1,a+1):
    print(i)
    if i==b:
        break
#%%
#숫자를 물어보게하고 입력된 숫자만큼 ★이 출력되게하시오(while 문으로)
a=int(input('숫자를 입력하세요'))
x=0
while x<a:
    x=x+1
    print(x*'★')
#%%
#숫자를 물어보게하고 위의 문제와 거꾸로된 삼각형이 출력되게하시오
a=int(input('숫자를 입력하세요'))
while a>0:  #5>0이 참이므로 아래의 실행문을 실행합니다.
   print(a*'★') #별 5개 출력
   a=a-1  
#%%
#주사위를 10000번 던져서 두개의 주사위의 눈의 합을 리스트에 넣으시오
import random
x=[]
i=0
dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
while i<10000:
    result1=random.choice(dice1)
    result2=random.choice(dice2)
    x.append(result1+result2)
    i=i+1
print(x)
print(len(x)) #a리스트 안의 요소의 갯수를 확인할 수 있습니다.
#%%
#위의 문제에서 두개의 주사위의 눈의 합이 10이 되는 확률을 구하시오
import random
x=[]
i=0
cnt=0
dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
while i<10000:
    result1=random.choice(dice1)
    result2=random.choice(dice2)
    if result1+result2==10:
        cnt=cnt+1
    i=i+1
print(cnt/10000)
#%%
#None개념 배우기
x=None
a=1
if a==1:
    x=[1,2,3]  #x 라는 변수에 리스트를 담았습니다
else:
    x='I love Python' #x라는 변수에 문자열을 담았습니다.
print(x)
#%%
#파이쎤은 사용가능한 정수의 범위가 정해져있지 않고 메모리가 허용하는 범위에서 지원
#가능한 수를 다 사용할 수 있습니다.
for i in range(1000000000000000000000000000000000000000000000000):
    a=i
    print(i)
#%%
#3의 2승을 파이썬으로 구하시오
print(3**2)
#루트4를 파이썬으로 구하세요
import math
print (math.sqrt(4))
#%%
#몬테카를로 알고리즘으로 원주율을 구하시오
import random
cnt=0
for i in range (1,10001):
    p1=random.uniform(0,1) #0~1 사이의 난수를 p1에 담습니다.
    p2=random.uniform(0,1)
    if p1**2+p2**2<=1: #부채꼴 안의 점이라면 
        cnt=cnt+1 #cnt를 1증가 시킵니다.
print(cnt/10000*4)
#%%
#실수형 자료 이해하기
#파이썬은 8바이트만 이용해서 수를 표현하기 때문에 학정된 범위의 수만 표현할 수 있습니다.
print(43.2-43.1)
#부도 소수형은 위와 같이 정밀도의 한계를 가지고 있습니다.
#IEEE754를 따르는 모든 컴퓨터 시스템의 문제입니다. IEEE754는 제한된 메모리를 이용해서
#실수를 표현하기 때문에 제한된 정밀도를 갖습니다.
#%%
#복소수형 자료 이해하기
c1=1+7j #1이 실수부, 7j 가 허수부
print(c1.real) #복소수형 자료에서 실수부만 취한다.
print(c1.imag) #복소수형 자료에서 허수부만 취한다.
c2=complex(2,3) #실수부가 2이고 허수부가 3인 복소수를 만든다.
print(c2)
#%%
#아래의 수학식의 답을 출력하시오 (1-2i)^2-2(1-2i)-12
c1=complex(1,-2)
print((c1**2)-(2*c1)-12)
