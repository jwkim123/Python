# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:27:07 2020
@author: jw
"""
#%%
#Q.주사위를 10번 던져 나오는 수를 확인하시오
import random
dice=[1,2,3,4,5,6]
for i in range(1,11):
    result = random.choice(dice)
    print(result)
#%%
#Q.주사위를 10번 던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오
import random
cnt=0
dice=[1,2,3,4,5,6]
for i in range(1,11): #아래의 실행문을 10번 수행하겠다
    result = random.choice(dice) #실행문1
    if result==3:         #실행문2
        cnt=cnt+1 #4칸 떼고 들어가야 if 문의 실행문이 된다.
print(cnt) #print는 변수안에 들어있는 값을 출력하는 함수
#%%
#Q.주사위를 10번 던져서 주사위의 눈이 짝수가 나오는 횟수를 출력하시오
import random
cnt=0
dice=[1,2,3,4,5,6]
for i in range(1,11):
    result=random.choice(dice)
    if result in (2,4,6): # in은 여러개의 값을 비교할 때 in 사용
        cnt=cnt+1
print(cnt)
#%%
#Q.주사위 2개를 동시에 20번 던져 눈의 합이 10이 되는 횟수를 출력하시오
import random #랜덤이라는 모듈을 실행하겠다 라는 뜻.
cnt=0
dice=[1,2,3,4,5,6]
for i in range(1,21): #20번 반복하기위한 루프문
    result1=random.choice(dice) #실행문1
    result2=random.choice(dice) #실행문2
    if result1+result2==10:
        cnt=cnt+1
print(cnt)
#%%
#Q.주사위 2개를 동시에 20번 던져서 눈의 합이 10이되는 확률을 구하시오
import random 
cnt=0
dice=[1,2,3,4,5,6]
for i in range(1,101): 
    result1=random.choice(dice) 
    result2=random.choice(dice) 
    if result1+result2==10:
        cnt=cnt+1
print(cnt/100)
#%%
#사칙 연산자 이해하기 
#+, -, *, /, sqrt, **
#나눈 나머지값 : %
#로그함수는 math 모듈을 import 해야합니다.
#log2는 밑수가 2인 로그함수
#log10은 밑수가 10인 로그함수
#모듈이름.함수이름(매개변수값)
#%%
#Q.밑수가 10이고 진수가 10인 log 값을 출력하시오
import math
print(math.log10(10)) #모듈이름.함수이름(매개변수값)
#%%
#Q.아래의 수학식을 파이썬으로 구현하시오
import math
a=math.log2(10)
print(2*a+((1/3)*a))
#%%
#연산자 축약
cnt+=1 # =>cnt = cnt+1
cnt-=1 # =>cnt = cnt-1
cnt*=2 # =>cnt = cnt*2
cnt/=4 # =>cnt = cnt/4
#%%
#Q.주사위를 10번 던져서 주사위의 눈이 3이 나오는 횟수를 출력하시오
#축약연산자 사용
import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,11):
    result=random.choice(dice)
    if result == 3:
        cnt+=1
print(cnt)
#%%
#Q.주사위를 20번 던져서 주사위의 눈이 4이상 나오는 횟수를 출력하시오
import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,21):
    result=random.choice(dice)
    if result>=4:
        cnt+=1
print(cnt)
#%%
#Q.주사위를 288회 던져서 주사위의 눈이 5이상 나오는 횟수를 출력하시오
import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,289):
    result=random.choice(dice)
    if result>=5:
        cnt+=1
print(cnt)
#%%
#Q.위의 문제의 확률을 구하시오
import random
dice=[1,2,3,4,5,6]
cnt=0
for i in range(1,289):
    result=random.choice(dice)
    if result>=5:
        cnt+=1
print(cnt/288)
#%%
#Q.위의 문제를 100번 반복해서 나오는 횟수를 출력하시오
import random
dice=[1,2,3,4,5,6]
for j in range(1,101):
    cnt=0
    for i in range(1,289):
        result=random.choice(dice)
        if result>=5:
            cnt+=1
    print(cnt)
#%%
#Q.위에서 출력된 결과를 리스트a에 담고 a리스트의 개수를 출력하시오
import random
a=[]
dice=[1,2,3,4,5,6]
for j in range(1,101):
    cnt=0
    for i in range(1,289):
        result=random.choice(dice)
        if result>=5:
            cnt+=1
    a.append(cnt)
print(len(a))
#%%
#Q.동젼을 100번 던져서 앞면이 나오는 횟수를 출력하시오
import random
coin=['앞면','뒷면']
cnt=0
for i in range(101):
    result=random.choice(coin)
    if result=='앞면':
        cnt+=1
print(cnt)
#%%
#Q.동전한개와 주사위한개를 동시에 100번 던져서 동전이 앞면이 나오고
#주사위의 눈이 5가 나오는 횟수를 출력하시오
import random
dice=[1,2,3,4,5,6]
coin=['앞면','뒷면']
cnt=0
for i in range(1,101):
    result1=random.choice(coin)
    result2=random.choice(dice)
    if result1=='앞면' and result2==5:
        cnt+=1
print(cnt)
#%%
#Q.위의 문제를 50번 반복해서 횟수가 50개가 출력되게하시오
import random
dice=[1,2,3,4,5,6]
coin=['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result1=random.choice(coin)
        result2=random.choice(dice)
        if result1=='앞면' and result2==5:
            cnt+=1
    print(cnt)
#%%
# Q.위의 결과 50개를 비어있는 a리스트에 담으시오
import random
a=[]
dice=[1,2,3,4,5,6]
coin=['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result1=random.choice(coin)
        result2=random.choice(dice)
        if result1=='앞면' and result2==5:
            cnt+=1
    a.append(cnt)
print(a)
#%%
#numpy 활용
#numpy는 딥러닝에 필요한 수학 공식 모음
import numpy as np #넘파이 모듈을 이 코드에서 사용하겠다.
b=[7,4,5,3,2]
print(np.mean(b))
#%%
#Q.numpy 활용하지 않고 평균값 출력
b=[7,4,5,3,2]
cnt=0
for i in b:
    cnt=i+cnt
print(cnt/5)
#%%
#Q.위의 a리스트의 요소들의 평균을 출력하시오(numpy이용)-1
import random
import numpy as np
a=[]
dice=[1,2,3,4,5,6]
coin=['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result1=random.choice(coin)
        result2=random.choice(dice)
        if result1=='앞면' and result2==5:
            cnt+=1
    a.append(cnt)
print(np.mean(a))
#%%
#Q.numpy 사용하지 않고 for loop문으로 평균값을 출력하시오-2
#sum활용
import random
a=[]
dice=[1,2,3,4,5,6]
coin=['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result1=random.choice(coin)
        result2=random.choice(dice)
        if result1=='앞면' and result2==5:
            cnt+=1
    a.append(cnt)
print(a)
print(sum(a)/50)
#%%
#Q.평균구하기-3 for loop활용
import random
a=[]
ct=0
dice=[1,2,3,4,5,6]
coin=['앞면','뒷면']
for j in range(1,51):
    cnt=0
    for i in range(1,101):
        result1=random.choice(coin)
        result2=random.choice(dice)
        if result1=='앞면' and result2==5:
            cnt+=1
    a.append(cnt)
print(a)
for k in a:
    ct=ct+k
print(ct/50)
#%%
#Q.주사위를 288번 던져서 주사위의 눈이 5이상이 나오는 횟수를 구하는 작업을
#100번 반복해서 그 횟수를 a리스트에 담고 평균, 분산, 표준편차를 구하시오
import random
import numpy as np
a=[]
dice=[1,2,3,4,5,6]
for j in range(1,101):
    cnt=0
    for i in range(1,289):
        result=random.choice(dice)
        if result>=5:
            cnt+=1
    a.append(cnt)
print(np.mean(a))
print(np.var(a))
print(np.std(a))
#%%
#Q.위 문제의 리스트의 요소들의 숫자가 90이상이고 106이하의 확률을 구하시오
import random
a=[]
cnt2=0
dice=[1,2,3,4,5,6]
for j in range(1,101):
    cnt=0
    for i in range(1,289):
        result=random.choice(dice)
        if result>=5:
            cnt+=1
    a.append(cnt)
for k in a:
    if k>=90 and k<=106:
        cnt2=cnt2+1
print(cnt2/100)
#%%
#판다스로 파이썬에 csv 파일 불러오기
import pandas as pd #판다스 모듈을 현 코드에서 사용하겠다고 함
emp=pd.read_csv("d:\\data\\emp3.csv") #d드라이브 밑에 emp3.csv를 읽어서 emp변수에 넣는다
print(emp) #emp테이블 프린트한다.
#%%
#판다스에서 데이터 검색
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(데이터프레임명[['컬럼명1', '컬럼명2']])
#%%
#Q.사원 테이블에서 이름과 월급을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','sal']])
#%%
#Q.select ename, sal, job, hiredate from emp;판다스로 구현하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','sal','job','hiredate']])
#%%
#Q.select ename, sal from emp where job='SALESMAN';
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','sal']] [emp['job']=='SALESMAN'])
#%%
#Q.월급이 1000이상 3000이상인 사원들의 이름과 월급을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','sal']] [emp['sal'].between(1000,3000)])
#%%
#Q.월급이 1000이상 3000이하가 아닌 사원들의 이름과 월급을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','sal']] [~emp['sal'].between(1000,3000)])
#%%
#Q.직업이 CLERK, SALESMAN인 사원들의 이름과 직업을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','sal']] [emp['job'].isin(['CLERK','SALESMAN'])])
#%%
#Q.직업이 clerk, salesman이 아닌 사원들의 이름과 직업을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','job']] [~emp['job'].isin(['CLERK','SALESMAN'])])
#%%
#Q.커미션이 null인 사원들의 이름과 커미션을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','comm']] [emp['comm'].isnull()]) #NaN=null
#%%
#Q.커미션이 null이 아닌 사원들의 이름, 커미션을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','comm']] [~emp['comm'].isnull()])
#%%
#Q.6개의 제품이 들어있는 상자에서 2개가 불량품이다. 제품검사를 위해
#3개를 추출했을 때 적어도 한개가 불량품일 확률은? (복원추출)
import random
cnt=0
box=['정상','정상','불량','정상','불량','정상']
for i in range(1,10001):
    result1=random.choice(box)
    result2=random.choice(box)
    result3=random.choice(box)
    if result1=='정상'and result2=='정상'and result3=='정상':
        cnt=cnt+1
print(1-cnt/10000)
#%%
#위 문제 another ans.
import random
box=[0,0,0,0,1,1]
cnt=0
for i in range(10001):
    test1=random.choice(box)
    test2=random.choice(box)
    test3=random.choice(box)
    if test1+test2+test3==0:
        cnt+=1
print(1-cnt/10000)
    
