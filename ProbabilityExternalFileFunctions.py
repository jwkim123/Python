# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:49:34 2020
@author: jw
"""
#%%
#Q.입력한 숫자가 3000보다 크면 숫자1, 작으면 숫자0을 리턴하는 함수를 생성하시오
def high_income(a):
    if a >3000:
        return 1
    else:
        return 0
    
b=[4000,5000,2000,3500,1000]
result=map(high_income,b)
print(list(result))

#%%
#Q.동전을 던져서 앞면이 나오는지 뒷면이 나오는지 출력하는 함수를 생성하시오
import random
def coin_cnt(num):
    coin=['앞면','뒷면']
    for i in range(num+1):
        result=random.choice(coin)
        print(result)
        
coin_cnt(5)

#%%
#Q.위의 코드를 수정해서 앞면이 나오는 확률을 출력하시오
import random
def coin_cnt(num):
    coin=['앞면','뒷면']
    cnt=0
    for i in range(num+1):
        result=random.choice(coin)
        if result=='앞면':
            cnt+=1
    return cnt/num

print(coin_cnt(100))

#%%
#Q.위의 함수를 사용해서 a리스트의 요소들을 적용해서 결과로 확률이 출력되게하시오
import random
def coin_cnt(num):
    coin=['앞면','뒷면']
    cnt=0
    for i in range(num+1):
        result=random.choice(coin)
        if result=='앞면':
            cnt+=1
    return cnt/num

a=[10,100,1000,10000,100000]
result2=map(coin_cnt,a)
print(list(result2))

#%%
#Q.주사위를 던져 눈이 5가 나오는 확률을 출력하는 함수를 생성하시오
import random
def dice_cnt(num):
    dice=list(range(1,7))
    cnt=0
    for i in range(num+1):
        result=random.choice(dice)
        if result==5:
            cnt+=1
    return cnt/num

a=[10,100,1000,10000,100000]
result2=map(dice_cnt,a)
print(list(result2))

#%%
#Q.8개의 제품중에 3개의 불량품이 있는 박스에서 랜덤하게 3개를 뽑는데
#그 중 2개가 불량품일 확률을 구하시오
import numpy as np
def box_cnt(num):
    box=['정상','정상','불량','정상','불량','정상','정상','불량']
    cnt=0
    for i in range(num+1):
        result=list(np.random.choice(box,3))
        if result.count('불량')==2:
            cnt+=1
    return cnt/num
        
a=[10,100,1000,10000,100000]
result2=map(box_cnt,a)
print(list(result2))

#%%
#read 함수를 이용해서 스티브잡스 연설문을 읽어오시오
f=open('d:\\data\\jobs.txt',encoding='UTF8')
data=f.read()
print(data)
f.close() 
#but 텍스트 파일의 용량이 매우 클 경우 read()로 한꺼번에 파일의 내용을 읽어들이는 것은
#메모리 문제를 야기시킬 수 있습니다.

#%%
#Q.중앙일보에서 검색한 기사를 파이썬으로 불러오고 빅데이터 라는 단어가 몇번나오는지 출력하시오
f=open('d:\\data\\mydata3.txt',encoding='UTF8')
data=f.read()
print(data)
print(data.count('빅데이터'))
f.close()

#%%
#Q.readline 함수를 이용해서 스티브잡스 연설문을 끝까지 읽어오시오
f=open('d:\\data\\jobs.txt',encoding='UTF8')
data=f.readline() #이 코드가 있어야 while문이 실행됩니다. 처음에 딱 한번만 실행
while data: #data변수 안에 data가 있으면 True, 없으면 False 입니다.
    print(data)
    data=f.readline() #그 다음줄을 읽어서 data변수에 입력합니다.
f.close()

#%%
#Q.한줄씩 읽은 데이터에서 인공지능이라는 단어가 나오면 카운트하시오
f=open('d:\\data\\mydata3.txt',encoding='UTF8')
cnt=0
data=f.readline() #이 코드가 있어야 while문이 실행됩니다. 처음에 딱 한번만 실행
while data: #data변수 안에 data가 있으면 True, 없으면 False 입니다.
    cnt=cnt+data.count('인공지능')
    data=f.readline() #그 다음줄을 읽어서 data변수에 입력합니다.
print(cnt)
f.close()

#%%
#Q.단어를 물어보게하고 해당 단어가 몇번 나오는지 출력하시오
f=open('d:\\data\\mydata3.txt',encoding='UTF8')
word=input('단어를 입력하세요')
cnt=0
data=f.readline() #이 코드가 있어야 while문이 실행됩니다. 처음에 딱 한번만 실행
while data: #data변수 안에 data가 있으면 True, 없으면 False 입니다.
    cnt=cnt+data.count(word)
    data=f.readline() #그 다음줄을 읽어서 data변수에 입력합니다.
print('이 기사에서 {}는 {}번 나왔습니다'.format(word,cnt))
f.close()

#%%
#write함수 이해하기. 화면에서 사용자 입력을 받고 파일로 쓰기
text=input('파일에 저장할 내용을 입력하세요')
f=open('d:\\data\\mydata.txt','w')
f.write(text)
f.close()

#%%
#Q.빨간색 공과 파란색공이 들어있는 상자에서 공 5개를 뽑아 그 중 파란공이 2개일 확률은?
import numpy as np
def box_cnt(num):
    box1=['red']*26
    box2=['blue']*24
    box=box1+box2
    cnt=0
    for i in range(num+1):
        result=list(np.random.choice(box,5))
        if result.count('blue')==2:
            cnt+=1
    return cnt/num
        
a=[10,100,1000,10000,100000]
result2=map(box_cnt,a)
print(list(result2))

#%%
#writelines 함수 이해하기
listdata=[2,2,1,3,8,5,7]
result=sorted(listdata) #리스트의 요소를 정렬한다.
print(result)
f=open("d:\\data\\mydata2.txt","w") #mydata2.txt를 생성하겠다.
f.write(str(result)) #result에 있는 내용을 문자열로 변환해서 mydata2.txt로 생성한다.
f.close()

#%%
#writelines 이해하기-2
data=[] #data라는 비어있는 리스트 생성
while True: #무한루프를 수행합니다.
    text=input('저장할 내용을 입력하세요')
    if text=='': #text에 아무것도 입력하지 않으면
        break #break문을 실행해서 무한루프를 종료합니다.
    data.append(text+'\n') #text가 엔터와 함께 data리스트에 append됩니다.
		
f=open('d:\\data\\mydata99.txt','w') #mydata99.txt를 생성하겠따
f.writelines(data) #data리스트의 내용을 mydata99.txt에 저장하겠다.
f.close()

#%%
#read, write txt
f=open("d:\\data\\mydata.txt","r") #r은 read입니다.
h=open("d:\\data\\mydata_copy.txt","w") #w는 write입니다.
data=f.read()
h.write(data)
f.close()
h.close()

#%%
#binary로 lena 사진 불러오고 복사하기
bufsize=1024 #1kb 크기의 버퍼 사이즈를
f=open("d:\\data\\lena.png","rb") #rb는 read binary의 약자
h=open("d:\\data\\lena_copy.png","wb")  #wb는 write binary의 약자
data=f.read(bufsize) #이미지를 1kb을 읽어서 data에 저장합니다.
while data: #data에 data가 발견되는 동안에 루프문을 수행합니다.
    h.write(data) #lena_copy.png에 1kb의 데이터씩 write 합니다.
    data=f.read(bufsize) #lena.png에서 1kb의 데이터를 read 합니다.
f.close()
h.close()
