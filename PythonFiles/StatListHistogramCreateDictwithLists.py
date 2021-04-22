# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:41:38 2020
@author: jw
"""
#%%
#Q.이메일을 출력하는데 도메인만 출력되게 하시오
import csv
file=open("d:\\data\\test.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
for emp_list in emp12_csv:
    add=emp_list[6].find('@') #@의 위치 인덱스번호찾고
    domain=emp_list[6][add+1:] #@전은 잘라내고 도메인만 남겨서 domain에 할당
    dot=domain.find('.') #domain에서 .의 위치 찾기
    print(domain[:dot]) #domain에서 첫번째 .앞까지 잘라내기

#%%
#리스트에 요소 추가하기
list_a=['a','b','c','d','e']
list_a.append('f') #append 메소드는 무조건 맨 뒤쪽에 요소를 추가한다.
print(list_a) #['a','b','c','d','e','f']
		
list_a.insert(3, 'k') #리스트의 3번째 위치에 k를 넣어라
print(list_a)  # ['a','b','c','k','d','e','f']

#%%
#Q.다음의 리스트에서 화성 뒤에 '소행성'을 추가하시오
a=['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
a.insert(a.index('화성')+1,'소행성') #넣을 곳 앞요소+1
print(a)

#%%
#Q.다음의 리스트에서 목성을 삭제하시오
a=['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
del(a[a.index('목성')])
print(a)

#%%
#Q.빨간공 2개와 파란공 3개가 들어있는 주머니에서 공을 하나 랜덤으로 추출하는데 비복원 추출로 하시오
import random
box=['red','red','blue','blue','blue']
ball=random.choice(box)
box.remove(ball)
print(box)

#%%
#Q.아래의 주머니에서 임의로 하나의 공을 뽑았을 때 그 공이 파란색일 확률은?
#복원 추출, 공 10000번 뽑기
import random
box=['red','red','blue','blue','blue']
cnt=0
for i in range(1,10001):
    ball=random.choice(box)
    if ball=='blue':
        cnt+=1
print(cnt/10000)

#%%
#Q.파란공 70개와 빨간공 30개가 들어있는 주머니를 만드시오
box1=['red']*30
box2=['blue']*70
box=box1+box2
print(box)

#%%
#Q.위의 박스안의 요소들을 무작위로 섞으시오
from random import shuffle #from 패키지 import 모듈
box1=['red']*30
box2=['blue']*70
box=box1+box2
shuffle(box) #무작위로 섞기
print(box)

#%%
#Q.위의 box에서 공 3개를 추출했을 떄 그 공 3개가 다 파란색일 확률은?
#비복원추출, 10000번 수행
from random import shuffle #from 패키지 import 모듈
import random
cnt=0
box1=['red']*30
box2=['blue']*70
box=box1+box2
shuffle(box) #무작위로 섞기
for i in range(1,10001):
    ball=random.sample(box,3) #box에서 공을 3개씩 추출해서 ball에 담기
    if ball.count('blue')==3: #ball에 blue가 3개면
        cnt+=1
print(cnt/10000)

#%%
#Q.이번에는 공 2개가 파란색일 확률은?
from random import shuffle #from 패키지 import 모듈
import random
cnt=0
box1=['red']*30
box2=['blue']*70
box=box1+box2
shuffle(box) #무작위로 섞기
for i in range(1,10001):
    ball=random.sample(box,3) #box에서 공을 3개씩 추출해서 ball에 담기
    if ball.count('blue')==2: #ball에 blue가 3개면
        cnt+=1
print(cnt/10000)

#%%
#Q.6개의 제품이 들어있는 상자가 있는데 그 중 2개가 불량품이라고 했을 때 
#제품 검사를 위해 3개를 추출했을 때 1개가 불량품일 확률은? (복원)
import random
import numpy as np
cnt=0
cnt2=0
box=['정상','불량','정상','정상','불량','정상']
for i in range(1,10001):
    ball=list(np.random.choice(box,3,replace=True))
    cnt+=1
    if ball.count('불량')==1:
        cnt2+=1
print(cnt2/cnt)

#%%
#Q.초등학생 10만명의 체중 데이터를 가지고 히스토그램 그래프를 그리시오
import matplotlib.pyplot as plt
import numpy as np
weight=np.random.randn(100000)*5+45
bins=list(range(30,61,2))
plt.hist(weight,bins,rwidth=0.8,color='magenta')
plt.xticks(bins)
plt.grid()

#%%
#Q.위의 체중 데이터를 모수로보고 10만명의 체중 데이터에서 100명을 샘플링하여 평균을 구하시오
import numpy as np
weight=np.random.randn(100000)*5+45
result=np.random.choice(weight,100,replace=True).mean()
print(result)

#%%
#Q.위의 작업을 1000번 수행해서 a라는 비어있는 리스트에 담으시오
import numpy as np
weight=np.random.randn(100000)*5+45
a=[]
for i in range(1,1001):
    a.append(np.random.choice(weight,100,replace=True).mean())
print(a)

#%%
#Q.위의 표본평균 1000개를 가지고 히스토그램 그래프를 그리시오
import numpy as np
import matplotlib.pyplot as plt
weight=np.random.randn(100000)*5+45
a=[]
for i in range(1,1001):
    a.append(np.random.choice(weight,100,replace=True).mean())
bins=list(range(40,61,1))
plt.hist(a,bins,rwidth=0.8,color='magenta')
plt.xticks(bins)
plt.grid()

#%%
#Q.우리반 나이 데이터를 비어있는 리스트 a에 입력하고 27살이 몇명있는지 출력하시오
import csv
file=open("d:\\data\\emp1222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
for emp_list in emp12_csv:
    a.append(int(emp_list[2]))
print(a.count(27))

#%%
#파이썬에서 정의된 모든 변수들 확인하기
a=[1,2,3,4,5]
b='scott'
c=30
print(dir())

#%%
#Q.emp2.csv에서 월급을 비어있는 리스트인 a에 담고 월급을 역순으로 정렳하시오
import csv
file=open("d:\\data\\emp22.csv",encoding='UTF8')
emp2_csv=csv.reader(file)
a=[]
for emp_list in emp2_csv:
    a.append(int(emp_list[5]))
a.sort(reverse=True)
print(a)

#%%
#enumerate 이해하기
emp12=['철수','짱구','유리','맹구']
result=list(enumerate(emp12))
print(result)

for i, k in enumerate(emp12):
    print(i,k)

#%%
#Q.아래의 music리스트에서 요소를 하나씩 빼내는데 앞에 인덱스번호도 함께 출력되게하시오
music=['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
artist=['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
for i, k in enumerate(artist):
    print(k,music[i])

#%%
#Q.가수와 음악제목으로 딕셔너리를 구성하시오
from collections import defaultdict
genie=defaultdict(list)
genie['비틀즈'].append('yesterday')
print(genie)
genie['비틀즈'].append('imagine')
print(genie)

#%%
#Q.위와같이 일일이 노가다하지말고 enumerate를 이용해서 genie 딕셔너리를 구성하시오
from collections import defaultdict
music=['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
artist=['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
genie=defaultdict(list)

for i,k in enumerate(artist):
    genie[k].append(music[i])
print(genie)

#%%
#Q.위의 genie 딕셔너리에서 음악만 추출하시오
for i in genie.values():
    for k in i:
        print(k)
        
for i in genie.values():
    print(i)
    
#%%
#Q.아래 코드를 수행해서 genie.values()의 요소들을 프린트 해보시오
from collections import defaultdict
music=['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
artist=['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
genie=defaultdict(list)

for i, k in enumerate(artist):
    genie[k].append(music[i])
for j in genie.values():
    print(j[0])
    
#%%
#Q.1.다음과 같이 결과를 출력하시오 yesterday,너랑나,beat it,imagine,마슈멜로우,smooth criminal
from collections import defaultdict
music=['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
artist=['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
genie=defaultdict(list)
a=[]

for i, k in enumerate(artist):
    genie[k].append(music[i])

for j in genie.values():
    m1=j[0]
    a.append(m1)
    
for k in genie.values():
    m2=k[1]
    a.append(m2)

bond=','
for b in a:
    b=bond.join(a)
print(b)

#%%
#Q.2.다음과 같이 결과를 출력하시오 yesterday,너랑나,beat it,imagine,마슈멜로우,smooth criminal
from collections import defaultdict
music=['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
artist=['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
genie=defaultdict(list)
for i, k in enumerate(artist):
    genie[k].append(music[i])

a=[]
b=[]
for j in genie.values():
    a.append(j[0])
    b.append(j[1])

bond=','
m=bond.join(a+b)
print(m)

#%%
#Q.3 without hardcoding
from collections import defaultdict
music=['yesterday','imagine','너랑나','마슈멜로우','beat it','smooth criminal']
artist=['비틀즈','비틀즈','아이유','아이유','마이클잭슨','마이클잭슨']
genie=defaultdict(list)
a=[]
for i,k in enumerate(artist):
    genie[k].append(music[i])
    a.append(artist.count(k))

b=[]
for n in range(max(a)):
    for j in genie.values():
        b.append(j[n])
        
bond=','
print(bond.join(b))
