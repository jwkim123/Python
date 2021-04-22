# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:49:48 2020
@author: jw
"""
#%%
#Q.아래의 txt 변수에서 w를 출력하시오
txt='A tale that was not right'
print(txt[12])
#맨 끝의 철자인 t를 출력하기
print(txt[-1])

#%%
#Q.emp2.csv에서 이름만 출력하는데 이름의 첫번째 철자, 소문자로 출력하시오
#판다스 아닌 버전:
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][0].lower())
    
#%%
#Q.다음의 SQL을 파이썬으로 구현하시오(판다스x)
#select ename, substr(ename,1,3) from emp;
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][:3])

#%%
#문자열 출력 이해하기
#문자열에서 홀수 번째 문자만 출력하기
txt='aAbBcCdDeEfFgGhHiIjJkK'
print( txt[0:] )  #0번째 부터 문자 끝까지 출력
print( txt[0 :: 2] ) #2칸씩 건너뛰면서 출력. 홀수번째 문자열만 출력
print( txt[1 :: 2] )#2칸씩 건너뛰면서 출력. 짝수번째 문자열만 출력
#문자열 거꾸로 만들기
result=txt[::-1] #문자열 전체를 뒤에 철자부터 거꾸로 읽어라 라는 뜻.
print(result)
print(txt[::])#문자열 전체 순서대로 출력
print(txt[:]) #문자열 전체 순서대로 출력
print(txt[::1]) #문자열 전체 순서대로 출력. 처음부터 끝까지 1스텝으로 읽는다.
#%%
#Q.이름을 출력하는데 이름의 철자를 거꾸로 출력하시오
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1][::-1])
    
#%%
#Q.아래의 SQL을 판다스를 이용하지 말고 파이썬으로 구현하시오
#select ename || job from emp;
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1]+emp_list[2])
    
#%%
#Q.다음과 같이 결과가 출력되게 하시오
#select ename||'의 직업은'||job||'입니다' from emp;
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1]+'의 직업은 '+emp_list[2]+'입니다.')
    
#%%
#Q.for loop문을 이용해서 숫자를 물어보게하고 해당 숫자만큼 1부터 출력하시오
num=int(input('숫자를 입력하세요'))
for i in range(1,num+1):
    print(i)
    
#%%
#Q.위의 코드를 수정해서 숫자를 물어보게하고 아래와 같이 ★이 출력되게 하시오
num=int(input('숫자를 입력하세요'))
for i in range(1,num+1):
    print(i*'★')
 
#%%
#Q.위의 문제에서처럼 삼각형을 출력하는데 거꾸로된 삼각형을 출력하시오
num=int(input('숫자를 입력하세요'))
for i in range(num,-1,-1):
    print(i*'★')

#%%
#Q.숫자를 물어보고 삼각형을 출력되게하는데 그 숫자만큼 커졌다 작아지는 삼각형을 출력하시오
num=int(input('숫자를 입력하세요'))
for i in range(1,num+1):
    print(i*'★')
for j in range(num-1,-1,-1):
    print(j*'★')
    
#%%
#Q.숫자를 물어보게하고 그 숫자크기의 정삼각형을 출력하시오
num=int(input('숫자를 입력하세요'))
for i in range(1,num+1):
    print(' '*(num-i)+i*'★')
    
#%%
#Q.가로, 세로의 숫자를 물어보게하고 해당 숫자만큼 사각형이 출력되게하시오
num1=int(input('가로의 숫자를 입력하세요'))
num2=int(input('세로의 숫자를 입력하세요'))
for i in range(1,num2+1):
    print(num1*'★')
    
#%%
#Q.emp2.csv에서 이름을 출력하는데 이름에 S를 포함하고 있는 사원들의 이름을 출력하시오
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    if 'S' in emp_list[1]:
        print(emp_list[1])
        
#%%
#Q.위의 문제에서 몇명의 사원이 있는지 출력하시오
import csv
cnt=0
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    if 'S' in emp_list[1]: #이름에 S자가 포함되어져 있으면
        cnt=cnt+1  #수행
print(cnt)

#%%
#Q.겨울왕국 스크립트에서 elsa라는 단어가 몇번 나오는지 카운트 하시오-1
winter=open('d:\\data\\winter.txt')
cnt=0
for i in winter: #winter.txt의 스크립트를 한행씩 가져오면서 
    if 'elsa' in i.lower(): #소문자로 변환해서 출력합니다.
        cnt+=1
print(cnt)
#틀린 코드
#이 코드는 한 행에 elsa가 두번 나와도  cnt는 1개만 카운트됩니다.

#%%
#Q.겨울왕국 스크립트에서 elsa라는 단어가 몇번 나오는지 카운트 하시오-2
winter=open('d:\\data\\winter.txt')
winter2=winter.read().split() #스크립트를 엔터로 먼저 줄 단위로 분리해야 함
cnt=0
for i in winter2: 
    if 'elsa' in i.lower(): #소문자로 변환
        cnt+=1
print(cnt)

#%%
#Q.파이썬으로 이름, 이름의 길이를 출력하시오
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],len(emp_list[1]))
    
#%%
#문자열이 알파벳(사람의 언어)인지 검색하기
txt1='Warcraft three'
txt2='안녕'
txt3='3PO'
print( txt1.isalpha() ) #False 중간에 공백이 false로 만듦
print( txt2.isalpha() ) #True. 한글이나 다른나라 언어도 True
print( txt3.isalpha() ) #False. 숫자가 하나라도 있으면 False

#%%
#Q.스티브잡스 연설문인 jobs.txt를 한행 한행씩 출력하시오
stev=open("d:\\data\\jobs.txt",encoding='UTF8')
stev2=stev.read().split()
for i in stev2:
    print(i)

#%%
#Q.위의 스크립트를 철자 하나씩 출력해서 이 스크립트에 알파벳이 몇개가 있는지 출력하시오
stev=open("d:\\data\\jobs.txt",encoding='UTF8')
stev2=stev.read().split()
cnt=0
for i in stev2:
    for k in i: #스크립트 한행을 읽어서 철자를 하나씩 불러오는 코드
        if k.isalpha()==True:
            cnt+=1
print(cnt)

#%%
#Q.위의 스크립트를 철자 하나씩 출력해서 이 스크립트에 숫자가 몇개가 있는지 출력하시오
stev=open("d:\\data\\jobs.txt",encoding='UTF8')
stev2=stev.read().split()
cnt=0
for i in stev2:
    for k in i: #스크립트 한행을 읽어서 철자를 하나씩 불러오는 코드
        if k.isdigit()==True:
            cnt+=1
print(cnt)

#%%
#알파벳과 숫자 동시에 확인하기
a='A story is 2003'
for i in a:
    if i.isalnum() == True:
        print( i )

#%%
#Q.긍정단어를 파이썬으로 읽어서 한행씩 출력하시오
positive=open("d:\\data\\positive-words.txt")
pos=positive.read().split()
for i in pos:
    print(i)
    
#%%
#Q.아래의 pos를 프린트해보세요
positive=open("d:\\data\\positive-words.txt")
pos=positive.read().split()
print(pos) #긍정단어들이 pos라는 리스트에 담겨져 있습니다.

#%%
#Q.아래의 단어가 긍정단어 리스트들 중에 있는지 확인하시오
if 'wonderful' in pos:
    print('존재합니다')
else:
    print('존재하지 않습니다.')

#%%
#위의 스티브잡스 연설문을 한 단어씩 출력하시오
stev=open("d:\\data\\jobs.txt",encoding='UTF8')
stev2=stev.read().split() #연설문을 어절별로 분리하여 stev2라는 리스트에 입력
for i in stev2: #stev2라는 리스트에서 하나씩 for 절 돌리는 것
    print(i)

#%%
#Q.emp2.csv에서 이름, 월급을 출력하시오
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    print(emp_list[1],emp_list[5])
    
#%%
#Q.사원 이름을 입력받고 대소문자에 상관없이 해당 사원의 이름, 월급을 출력하시오
employee=input('이름을 입력하세요')
import csv
file=open("d:\\data\\emp22.csv")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    if emp_list[1].lower()==employee.lower():
        print(emp_list[1], emp_list[5])
        
#%%
#Q.스티브잡스 연설문에서는 정관사 the가 몇번 나오는가?
stev=open("d:\\data\\jobs.txt",encoding='UTF8')
stev2=stev.read().split()

cnt=0
for i in stev2:
    if i.lower().strip()=='the': #양쪽에 공백이 있을지도 모르고 대소문자 구분없이 검색
        cnt+=1
print(cnt)

#%%
#문자열에서 특정 문자 개수 구하기
txt='A lot of things occur each day. Today is beautiful day'
print(txt.count('day')) #txt에서 day 단어의 건수를 확인 
      
#%%
#Q.안철수 연설문에서 '국민'이라는 단어가 몇번 나오는지 카운트하시오
ahn=open("d:\\data\\ahn.txt",encoding='UTF8')
ahn2=ahn.read() #split 안하고 그냥 안철수 연설문을 읽어서 통째로 ahn2에 입력
print(ahn2) #안철수 연설문 전체가 출력
print(ahn2.count('국민')) #연설문 전체에서 '국민'이라는 단어가 몇개인지 출력

#%%
#파이썬에서 막대 그래프 그리는 방법
import matplotlib.pyplot as plt
y_value=[21.6,23.6,45.8,77.0]
x_index=[0,1,2,3]
plt.bar(x_index, y_value,color='blue')
plt.title('Coin Probability') #그래프 제목
plt.xlabel('# of Coin Heads') #그래프 x축 라벨
plt.ylabel('probability') #그래프 y축 라벨
plt.show()

#%%
#Q.동전을 10번 던져서 앞면이 나올 확률을 나타내는 막대 그래프를 시각화하시오
def coin_prob(num):
    import random
    coin=['앞면','뒷면']
    cnt=0
    for k in range(1,10001):
        a=[]
        for i in range(1,11):
            a.append(random.choice(coin))
        if a.count('앞면')==num:
            cnt+=1
    return cnt/10000

import matplotlib.pyplot as plt
for j in range(0,11):
    y_value=coin_prob(j)
    x_index=j
    plt.bar(x_index,y_value,color='magenta')
plt.title('Coin Probability') #그래프 제목
plt.xlabel('# of Coin Heads') #그래프 x축 라벨
plt.ylabel('probability') #그래프 y축 라벨
plt.show()
