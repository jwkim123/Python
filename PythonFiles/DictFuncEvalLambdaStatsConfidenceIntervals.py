# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:35:58 2020
@author: jw
"""
#%%
#Q.아래의 리스트의 짝수번째 요소의 합을 출력하시오
listdata=[2,2,1,3,8,4,3,9,2,20]
result=sum(listdata[1::2])
print(result)

#%%
#Q.아래의 리스트 a에서 없는 숫자 하나를 찾으시오
a=[2,1,5,4,6,7,9,10,3]
result=sum(range(1,11))-sum(a)
print(result)

#%%
#Q.다음의 리스트를 사전형으로 구성하시오
sol_eng=['sun','mercury','venus','earth','mars']
sol_kor=['태양','수성','금성','지구','화성']
sol={}
for i, j in zip(sol_eng, sol_kor):
    sol[j]=i
print(sol)

#%%
#Q.아래의 딕셔너리 값 중에서 fire를 피땀눈물로 변경하시오
dict={'방탄소년단':'Fire','소녀시대':'Gee'}
dict['방탄소년단']='피땀눈물'
print(dict)

dict1={'소녀시대':['다시만난세계','Gee'], '방탄소년단':['DNA','Fire'] }
dict1['방탄소년단'][1]='피땀눈물'
print(dict1)

#%%
#Q.아래의 딕셔너리에서 다시만난세계의 값만 지우시오
dict={'소녀시대':['다시만난세계','Gee'], '방탄소년단':['DNA','Fire'] }
del dict['소녀시대'][0]
print(dict)

#%%
#Q.sol 사전에 있는 키를 추출해서 키 값만 추출하시오
sol={'태양':'sun', '수성':'mercury', '금성':'venus', '지구':'earth', '화성':'mars'}
for i in sol.keys():
    print(i,end=',') #end는 옵션에 준 구분자로 값들을 가로로 출력하면서 구분자로 구분합니다.
    
#%%
#Q.아래의 genie 딕셔너리에서 값만 추출하시오
genie={'비틀즈':['yesterday','imagine'],'아이유':['너랑나','마슈멜로우'],'마이클 잭슨':['beat it','smooth criminal']}
for i in genie.values():
    print(i)
    
#%%
#Q.위의 값을 추출한 것에서 0번째 요소만 출력하시오
genie={'비틀즈':['yesterday','imagine'],'아이유':['너랑나','마슈멜로우'],'마이클 잭슨':['beat it','smooth criminal']}
for i in genie.values():
    print(i[0])

#%%
#Q.genie 딕셔너리의 값들을 리스트로 만들고 shuffle 로 섞어보시오
from random import shuffle
genie={'비틀즈':['yesterday','imagine'],'아이유':['너랑나','마슈멜로우'],'마이클 잭슨':['beat it','smooth criminal']}
genie2=list(genie.values())
shuffle(genie2)
print(genie2) #앞에 dict_values가 안나오게 하려면 list()로 한번 감싸주기

#%%
#Q.아티스트별로 노래가 겹치지 않게 하는데 shuffle함수를 이용해서 코드를 수행할때마다 곡이 무작위로 섞여서 출력되게하시오
from random import shuffle
genie={'비틀즈':['yesterday'],'아이유':['너랑나','마슈멜로우'],'마이클 잭슨':['beat it','smooth criminal','billy jean']}
genie2=list(genie.values())
shuffle(genie2)

b=[]
for i in range(len(genie2)):
    b.append(len(genie2[i]))
#print(b)

c=[]
for j in range(max(b)):
    for k in genie2:
        if len(k)>j:
            c.append(k[j])

print(','.join(c))

#%%
#dict 요소 추출 이해하기
genie={'비틀즈':['yesterday','imagine'],'아이유':['너랑나','마슈멜로우'],'마이클 잭슨':['beat it','smooth criminal']}
print(list(genie.keys()))#['비틀즈', '아이유', '마이클 잭슨'])
print(list(genie.values())) #[['yesterday', 'imagine'], ['너랑나', '마슈멜로우'], ['beat it', 'smooth criminal']])
print(list(genie.items())) #[('비틀즈', ['yesterday', 'imagine']), ('아이유', ['너랑나', '마슈멜로우']), ('마이클 잭슨', ['beat it', 'smooth criminal'])])

#%%
#Q.genie딕셔너리의 요소들을 리스트에 담고 음악 첫번째 곡들만 출력하시오
genie={'비틀즈':['yesterday','imagine'],'아이유':['너랑나','마슈멜로우'],'마이클 잭슨':['beat it','smooth criminal']}
result=list(genie.items())
for i in result:
    print(i[1][0])
    
#%%
#Q.우리반 테이블에서 이름, 통신사를 출력하시오
import csv
file=open("d:\\data\\emp12222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
for emp_list in emp12_csv:
   print(emp_list[1],emp_list[5])
   
#%%
#Q.우리반데이터에서 통신사를 key로 하고 학생이름을 값으로해서 defaultdict를 생성하시오
from collections import defaultdict
import csv
file=open("d:\\data\\emp12222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)

telecom=defaultdict(list)
for emp_list in emp12_csv:
   telecom[emp_list[5]].append(emp_list[1])
   
result=telecom['kt']
print(sorted(result))

#%%
#Q.알파벳 대문자를 출력하고 ord함수를 이용해서 컴퓨터언어로 변경하시오
import string
for i in string.ascii_uppercase:
    print(i,'--->',ord(i))

#%%
#Q.아래와 같이 결과를 출력하시오 65--->A, 66--->B,....
import string
for j in range(65,91):
    print(j,'--->',chr(j))
    
#%%
#Q.다음의 식을 계산하시오 34+256-71*34=?
a='34+256-71*34'
print(a,'=',eval(a))

#%%
#Q.다음의 리스트의 숫자를 뽑아내서 각각 더하는 모양의 문자열을 생성하고 계산하시오
a=[34,22,45,27,31,33,55]
b=[]
for i in a:
    b.append(str(i))

result='+'.join(b)
print(result,'=',eval(result))

#%%
#Q.우리반 데이터에서 나이를 읽어들여 다 합한 결과를 출력하시오
import csv
file=open("d:\\data\\emp12222.csv",encoding='UTF8')
emp12_csv=csv.reader(file)
a=[]
for emp_list in emp12_csv:
    a.append(emp_list[2])

result='+'.join(a)
print(result,'=',eval(result))

#%%
#Q.다음 함수를 lambda 함수로 만들어 보시오
#def gob_func(a,b):
    #return a*b
k=lambda a:'even' if (a%2==0) else 'odd'
print(k(3))

#%%
#Q.다음의 함수를 lambda로 구현하시오
k=lambda a:'고소득자입니다' if (a>=3000) else '일반소득자입니다'
print(k(2000))

#%%
#Q.평균140 표준편차5를 이용해서 신뢰구간 95%안에 있는지 확인하시오
def child_tall(num):
    if 140-1.96*5<=num<=140+1.96*5:
        return '신뢰구간 95%안에 있습니다.'
    else:
        return '신뢰구간 95%안에 없습니다.'
        
print(child_tall(180))

#%%
#Q.신뢰구간 95%일때의 그래프를 시각화 하시오
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x=np.arange(120,160,0.001)
y=norm.pdf(x,140,5) #확률밀도함수
plt.plot(x,y,color='red')
plt.fill_between(x,y,where=(x>=140-1.96*5) & (x<=140+1.96*5),color='pink',alpha=0.5)
plt.show
#where가 색칠하는 구간을 지정합니다.

#%%
#Q.신뢰구간 95, 99, 68일때의 그래프를 시각화 하시오
def confidence_interval(num):
    if num==95: 
        a=1.96
    elif num==99:
        a=2.58
    else:
        a=1

    lower=140-a*5
    upper=140+a*5

    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm

    x=np.arange(120,160,0.001)
    y=norm.pdf(x,140,5) #확률밀도함수
    plt.plot(x,y,color='magenta')
    plt.fill_between(x,y,where=(x>=lower) & (x<=upper),color='pink',alpha=0.5)
    return plt.show

confidence_interval(95)
confidence_interval(99)
confidence_interval(68)
