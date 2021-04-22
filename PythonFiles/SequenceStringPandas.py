  
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:31:03 2020
@author: jw
"""
#%%
#Q.판다스로 이름이 SCOTT인 사원의 이름, 월급을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','sal']] [emp['ename']=='SCOTT'])
#%%
#시퀀스 자료형 이해하기
"""시퀀스 자료형은 어떤 객체가 순서를 가지고 나열되어 있는 것을 말합니다.
문자열 'abcd'는 문자 a,b,c,d가 순서를 가지고 차례대로 나열되어 있는 것입니다."""

#%%
#Q.scott을 담은 문자형 변수 a에서 알파벳 o를 출력하시오
a='scott'
print(a[2])
#%%
#Q.다음의 문자형 변수 b에서 맨 끝의 철자인h를 출력하시오 b='smith'
b='smith'
print(b[-1])
#%%
#Q.판다스를 이용해서 emp3.csv.에서 이름을 출력하는데 첫번째 철자만 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']: #emp3.csv에서 ename만 가져와서 ename의 개수만큼 loop문을 수행해서
    print(i[0]) #ename의 첫번째 글자를 출력합니다.
#%%
#for loop문을 안쓰고 그냥 print(type(ename['ename'])) 하면 <class 'pandas.core.series.Series>
#가 나오는데 이거를 문자형으로 변경하려면 for loop문을 이용해서 하나씩 <class 'str'>
#로 변경해줘야 합니다.
#%%
#Q.판다스를 이용해서 emp3.csv.를 가져와서 이름의 끝글자를 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    print(i[-1])
#%%
#Q.위의 결과에서 앞에 이름도 같이 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    print(i,i[-1])  #or 사이에 공백을 주고 싶으면 print(i,'  ',i[-1])
#%%
#Q.이름의 첫번째 철자가 S로 시작하는 사원들의 이름을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    if i[0] =='S':
        print(i)
#%%
#Q.이름의 끝글자가 T로 끝나는 사원들의 이름을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    if i[-1] =='T':
        print(i)
#%%
#Q.이름의 두번째 철자가 M인 사원의 이름을 출력하시오
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    if i[1] =='M':
        print(i)
#%%
#시퀀스 자료 슬라이싱 이해하기
a='scott'
print(a[1:3]) #1부터 3번째 자리까지 라는 뜻인데 3번쨰 자리는 출력하지 않음
#%%
#Q.다음의 SQL을 판다스로 구현하시오 select substr(ename,1,3) from emp;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    print(i[0:3])
#%%
#Q.다음의 SQL을 판다스로 구현하시오 select substr(ename,-2,2) from emp;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    print(i[-2:])
#%%
#Q.아래의 SQL을 판다스로 구현하시오 select substr(ename,2,3) from emp;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in emp['ename']:
    print(i[1:4])
#%%
#Q.두개의 리스트를 연결하시오
a=[2,3,4,5]
b=[9,2,4,8]
print(a+b)
#%%
#Q.다음의 SQL을 판다스로 구현하시오 select ename||sal from emp;
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i, k in zip(emp['ename'],emp['sal']):
    print(i+str(k))
#zip함수를 for loop 문에 사용하게 되면 두개의 범위 데이터를 한번에 받아서 loop를
#수행할 수 있습니다.
#%%
#시퀀스 자료 반복 이해하기(*)
print('a'*7)
print([1,2,3]*5)
#%%
#Q.주사위의 눈 6개를 100개 담은 리스트 dice100을 만드시오
b=[1,2,3,4,5,6]
print(b*100)
#%%
#Q.초등학생 키가 10개가 들어있는 아래의 tall리스트의 요소 10개를 10000개로 증가시켜 출력하시오
tall=[129.3,130.2,132.5,134.7,136.3,1378.,138.1,140.2,142.3,145.2]
tall10000=tall*1000
print(len(tall10000))
#%%
#위의 모집단의 평균값, 분산, 표준편차를 출력하시오
import numpy as np
tall=[129.3,130.2,132.5,134.7,136.3,137.8,138.1,140.2,142.3,145.2]
tall10000=tall*1000
print(np.mean(tall10000))
print(np.var(tall10000))
print(np.std(tall10000))
#%%
#Q.위의 모집단 tall10000에서 표본을 20개를 랜덤으로 추출하시오
import random
tall=[129.3,130.2,132.5,134.7,136.3,137.8,138.1,140.2,142.3,145.2]
tall10000=tall*1000 #초등학생 키 데이터 10000개 생성(모집단 생성)
for i in range(1,21): #20번 반복하면서 
    print(random.choice(tall10000)) #모집단에서 랜덤으로 키 하나씩 추출
#%%
#Q.위의 랜덤으로 추출한 표본 20개를 비어있는 a리스트에 담으시오
import random
a=[]
tall=[129.3,130.2,132.5,134.7,136.3,137.8,138.1,140.2,142.3,145.2]
tall10000=tall*1000 #초등학생 키 데이터 10000개 생성(모집단 생성)
for i in range(1,21): #20번 반복하면서 
    a.append(random.choice(tall10000)) #모집단에서 랜덤으로 키 하나씩 추출
print(a)
#%%
#
import numpy as np
import random
a=[]
tall=[129.3,130.2,132.5,134.7,136.3,137.8,138.1,140.2,142.3,145.2]
tall10000=tall*1000 #초등학생 키 데이터 10000개 생성(모집단 생성)
for i in range(1,21): #20번 반복하면서 
    a.append(random.choice(tall10000)) #모집단에서 랜덤으로 키 하나씩 추출
print(np.mean(a))
#%%
#시퀀스 자료 크기 이해하기(len)
a='scott'
print(len(a))

b=[2,3,4,8,1]
print(len(b))
#%%
#Q.아래의 SQL을 판다스로 구현하시오 select ename, length(ename) from emp;import pandas as pd
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
for i in (emp['ename']):
    print((i),len(i))
#%%
#모평균이 30이고 모표준편차가 7인 모집단을 구성하시오
import numpy as np
avg=30
std=7
N=1000000
mogipdan=np.random.randn(N)*std+avg #np.random.randn(숫자)를 쓰면 이 숫자만큼
print(mogipdan)      #가우시안 정규분포에 따르는 난수들이 숫자만큼 생성됩니다.
#%%
#위의 모평균을 구하시오
import numpy as np
avg=30
std=7
N=1000000
mogipdan=np.random.randn(N)*std+avg #np.random.randn(숫자)를 쓰면 이 숫자만큼
print(np.mean(mogipdan)) 
#%%
#Q.다음 SQL을 판다스로 구현하시오 select ename, sal from emp where job in ('SALESMAN','ANALYST')
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','job']] [emp['job'].isin(['SALESMAN','ANALYST'])])
#%%
#Q.다음SQL을 판다스로 구현하시오select ename, job from emp where job not in ('SALESMAN',''ANALYST)
import pandas as pd
emp=pd.read_csv("d:\\data\\emp3.csv")
print(emp[['ename','job']] [~emp['job'].isin(['SALESMAN','ANALYST'])])
#%%
#Q. <"모집단"의 모평균은> 이라는 문자열을 출력하시오
print(""" "모집단"의 모평균은 """)
print(""" "모집단"의 모표준편차는 """)
print(""" "모집단"의 모분산은 """)
#%%
#Q.모평균이 30이고 모표준편차가 7인 모집단의 모평균과 모분산과 모표준편차를 아래와같이 출력하시오
import numpy as np
avg=30
std=7
N=1000000
mogipdan=np.random.randn(N)*std+avg #np.random.randn(숫자)를 쓰면 이 숫자만큼
print(""" "모집단"의 모평균은 """,np.mean(mogipdan))
print(""" "모집단"의 모표준편차는 """,np.std(mogipdan))
print(""" "모집단"의 모분산은 """,np.var(mogipdan))
#%%
#Q.
import numpy as np
avg=30
std=7
N=1000000
mogipdan=np.random.randn(N)*std+avg 
print(np.random.choice(mogipdan,49))
#%%
#위에서 뽑은 49개의 평균값을 출력하시오
import numpy as np
avg=30
std=7
N=1000000
mogipdan=np.random.randn(N)*std+avg 
print(np.random.choice(mogipdan,49).mean())
#%%
#Q.이번에는 비어있는 리스트a를 선언하고 a에 100개를 담고
#표본평균의 평균값과 표준편차를 출력하시오
import numpy as np
avg=30
std=7
N=1000000
a=[]
mogipdan=np.random.randn(N)*std+avg 
for i in range(1,101):
    a.append(np.random.choice(mogipdan,49).mean())
print(""" "표본평균" 의 평균값은 """,np.mean(a))
print(""" "표본평균" 의 표준편차값은 """,np.std(a))
print(""" "표본평균" 의 분산값은 """,np.var(a))
#%%
#Q.나는 자바보다 파이썬에 익숙합니다 를 출력하시오
txt1 = '자바'
txt2 = '파이썬'
num1 = 5
num2 = 10
print('나는 %s 보다 %s 에 더 익숙합니다.' %(txt1, txt2))
#%%
#5는 10보다 작습니다. 를 출력하시오
num1=5
num2=10
print('%d는 %d 보다 작습니다.' %(num1, num2))
#%%
#Q.위의 문제의 값을 '표본평균의 평균값은...이고 분산값은...이고 표준편차는...입니다'
#로 출력되게 하시오(문자열 포맷 이용, 소수점 2번째 자리에서 반올림)
import numpy as np
avg=30
std=7
N=1000000
a=[]
mogipdan=np.random.randn(N)*std+avg 
for i in range(1,101):
    a.append(np.random.choice(mogipdan,49).mean())
b=round(np.mean(a),2)
c=round(np.std(a),2)
z=round(np.var(a),2)
print('표본평균의 평균값은 %.2f이고 분산값은 %.2f이고 표준편차는 %.2f 입니다.' %(b,c,z))
#%%
#Q.어느 비행기 탑승객의 짐의 무게는 평균이18kg이고 표준편차가 3kg인 정규분포를 따른다.
#이 비행기 탑승객 중에서 36명을 임의추출할 때, 짐의 평균무게가 17kg이상일 확률을 구하여라
import numpy as np
avg=18
std=3
cnt=0
pop=np.random.randn(i)*std+avg
for i in range(1,10000):
    if np.random.choice(pop,36).mean() >=17:
        cnt+=1
print(cnt/10000)
