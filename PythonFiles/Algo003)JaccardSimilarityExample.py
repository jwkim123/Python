# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:44:07 2020
@author: jw
"""
#%%
#파이썬에서 합집합과 교집합 구하기
a={1,2,3,4}
b={2,4,5}
print(type(a)) #<class 'set'>

#a와 b의 합집합 구하기
union_set=a.union(b)
print(union_set) #{1,2,3,4,5}

#a와 b의 교집합 구하기
intersect_set=a.intersection(b)
print(intersect_set) #{2,4}

#a와 b의 자카드 유사도 구하기
print(len(intersect_set)/len(union_set)) #0.4

#%%
#리스트로 합집합과 교집합 구하기
a=[1,2,3,4]
b=[2,4,5]

#a와 b의 합집합 구하기
union_set=set(a+b)
print(union_set) #{1,2,3,4,5}

#a와 b의 교집합 구하기
intersect_set=[]
for i in a:
    if i in b:
        intersect_set.append(i)
print(intersect_set) #[2,4]

#%%
#Q.교집합, 합집합 구하기
a=[1,1,1,2,2,3]
b=[1,1,2,2,4,5]
#교집합부터 구하기
inter=[]
for i in a:
    if i in b:
        b.remove(i)
        inter.append(i)
print(inter)  

b=inter+b
print(b)


#합집합 구하기  
hap=[]
hap=a+b
for i in range(len(inter)):
    if i in hap:
        hap.pop(hap.index(inter[i]))
        
print(hap)

#%%
#Q.교집합, 합집합 구하기- Collection 이용
import collections

a = [1,1,1,2,2,3]
b = [1,1,2,2,4,5]

intersection = []
result = collections.Counter(a) & collections.Counter(b) # 교집합
intersection = list(result.elements()) # 요소만 리스트로 빼내오기

result2 = collections.Counter(a) | collections.Counter(b) # 합집합
union = list(result2.elements())       # 요소만 리스트로 빼내오기

print(intersection)
print(union)

#%%
#Q.두 문장을 받아서 두개의 철자로 분리하여 리스트에 저장하고 알파벳2개씩 자르기
str1=input('문자열을 입력하세요').upper()
str2=input('문자열을 입력하세요').upper()

def str_split(string):
    res=[]
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            res.append(string[i:i+2])
    return res

print(str_split(str1))
print(str_split(str2))

#%%
#Q.교집합과 합집합 구하기
str1=input('문자열을 입력하세요').upper()
str2=input('문자열을 입력하세요').upper()

def str_split(string):
    res=[]
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            res.append(string[i:i+2])
    return res

a=str_split(str1)
b=str_split(str2)

#교집합
intersection=[]
for i in a:
    if i in b:
        intersection.append(i)
print(intersection) #['FR','NC']

#합집합
union=set(a+b)
print(union) #{'CH','AN'.'CE','EN','FR','RE','RA','NC'}

#%%
#Q.위 함수 a,b의 자카드 유사도 구하기
len_i=len(intersection)
len_u=len(union)
print(math.trunc(len_i/len_u*65536)) #16384.0

#%%
#Q.위의 함수들을 합치시오
import math
def str_split(string):
    res=[]
    for i in range(len(string)-1):
        if string[i].isalpha() and string[i+1].isalpha():
            res.append(string[i:i+2])
    return res

def Jaccard():
    str1=input('문자열을 입력하세요').upper()
    str2=input('문자열을 입력하세요').upper()
    a=str_split(str1)
    b=str_split(str2)
    intersection=[]
    for i in a:
        if i in b:
            intersection.append(i)
            
    union=set(a+b)
    
    len_i=len(intersection)
    len_u=len(union)
    try:
        math.trunc(len_i/len_u*65536)
    except ZeroDivisionError:
        return 65536

print(Jaccard())

#%%
#Q.완성ver.
def jaccard_kakao():
    str1=input('Enter first word').upper()
    str2=input('Enter second word').upper()
    #split characters into 2
    if len(str1)>=2 and len(str1)<=1000 and len(str2)>=2 and len(str2)<=1000:
        s_list1=[str1[i:i+2] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
        s_list2=[str2[i:i+2] for i in range(len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    else: 
        print('only between 2 and 1000 characters are allowed ')

    #find intersection
    intsct=[]
    for j in s_list1:
        if j in s_list2:
            intsct.append(j)
    
    #find union set
    union=s_list1+s_list2
    for h in intsct:  
        union.remove(h)
    
    #calculation
    if len(union)!=0:
        return (int((len(intsct)/len(union))*65536))
    else:
        return 65536
    

print(jaccard_kakao())

#france, french
#handshake, shake hands
#aa1+aa2, AAAA12
#E=M*C^2, e=m*c^2
